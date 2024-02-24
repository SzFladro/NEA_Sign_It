from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTimer, QUrl, Qt, QThread, Signal, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLayout, QLineEdit, QMainWindow, QProgressBar,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget, QLabel, QPushButton)
from PySide6.QtMultimedia import QMediaDevices, QCamera
import cv2
import numpy as np
import os
import time
import mediapipe as mp
import string
import tensorflow as tf


from DataBase import config
from Interface import Notifications

config_cam = config.Config()
camerainput = config_cam.get_main_camera()
model = tf.keras.models.load_model(u'Translator/BSLmodel.h5')
model.load_weights(u'Translator/BSLweights.h5')
mp_holistic = mp.solutions.holistic # Holistic model
mp_drawing = mp.solutions.drawing_utils # Drawing utilities

notificationhandler = Notifications.NotificationHandler

signs = list(string.ascii_uppercase)
AvailableWords = np.array(signs)

class VideoThread(QThread):
    change_ImageSignal = Signal(np.ndarray)
    frames_ready = Signal(list)
    prediction_ready = Signal(str)

    def __init__(self, camera_index):
        super().__init__()
        self._run = False
        self.camera_index = camera_index
        self.frames =[]
        self.collect_frames = False

    def run(self):
        cap = cv2.VideoCapture(self.camera_index)
        self._run = True
        frame_count = 0
        frame_max_count = 30
        try:
            with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
                while self._run:
                    ret, cv_img = cap.read()
                    if ret:
                        image, results = self.mediapipe_detection(cv_img, holistic)
                        self.draw_styled_landmarks(image,results)  
                        self.change_ImageSignal.emit(image)
                        if self.collect_frames:
                            keypoints = self.extract_keypoints(results)
                            self.frames.append(keypoints)
                            frame_count += 1
                            if frame_count == frame_max_count:
                                self.collect_frames = False
                                prediction = model.predict(np.expand_dims(self.frames, axis=0))[0]
                                predicted_word = AvailableWords[np.argmax(prediction)]
                                self.prediction_ready.emit(predicted_word)
                                self.frames_ready.emit(self.frames)
                                self.frames = []  
                                frame_count = 0
                    else:
                        frame_count = 0

                    time.sleep(0.1)  
        finally:
            cap.release()

    def stop(self):
        self._run = False
        self.wait()

    def start_collecting_frames(self):
        self.collect_frames = True

    ##method for processing frames and locating the hands,face,pose from the image
    def mediapipe_detection(self,image, model):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
        image.flags.writeable = False                  # locks the image so that it isnt writable
        results = model.process(image)                 # Make prediction
        image.flags.writeable = True                   # unlocks the image to allow for connections to be drawn on 
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
        return image, results

    ##method for drawing the different connections to the frame using the coordinates of the different parts collected (landmarks)
    def draw_styled_landmarks(self,frame, results):
        # Draw face connections
        mp_drawing.draw_landmarks(frame, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION, 
                                 mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1), 
                                 mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)) 
        # Draw pose connections
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4), 
                                 mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)) 
        # Draw left hand connections
        mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4), 
                                 mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)) 
        # Draw right hand connections  
        mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4), 
                                 mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)) 
        
    ##method for collecting seperating the different coordinates into their respective groups and storing it as an array
    def extract_keypoints(self,results):
        pose = np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
        face = np.array([[landmark.x, landmark.y, landmark.z] for landmark in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(468*3)
        lefthand = np.array([[landmark.x, landmark.y, landmark.z] for landmark in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
        righthand = np.array([[landmark.x, landmark.y, landmark.z] for landmark in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
        return np.concatenate([pose, face, lefthand, righthand])

class LiveInterface:
    UI = None
    camera_on = False
    thread = None
    TypedWord = None

    @classmethod
    def set_mode(cls,Livemode):
        cls.mode = Livemode

    @classmethod
    def set_ui(cls, ui_instance):
        cls.UI = ui_instance
        cls.frame_width = cls.UI.LiveCVframe.width()
        cls.frame_height = cls.UI.LiveCVframe.height()
        cls.Live_Controls()

    @classmethod
    def Live_Controls(cls):
        cls.UI.ToggleCamera.clicked.connect(cls.CameraControls)
        cls.UI.LiveContinueButton.clicked.connect(cls.ready_Up)
        cls.UI.LiveAddtoTypedButton.clicked.connect(lambda: cls.pushtoType())
        cls.UI.LiveToTranslatorButton.clicked.connect(cls.returnbacktoUI)

    @classmethod
    def update_image(cls, cv_img):
        if cls.camera_on:
            qt_img = cls.convert_cv_qt(cv_img)
            cls.UI.LiveFootageLabel.setPixmap(qt_img)

    @classmethod
    def convert_cv_qt(cls, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        # Scale the image to match the dimensions of the LiveCVframe
        scaled_image = convert_to_Qt_format.scaled(cls.frame_width, cls.frame_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
        return QPixmap.fromImage(scaled_image)

    @classmethod
    def CameraControls(cls):
        if cls.camera_on:
            cls.stop_camera()
        else:
            cls.start_camera()

    @classmethod
    def returnbacktoUI(cls):
        print(cls.mode)
        if cls.mode == "Bee":
            cls.stop_camera()
            cls.mode = None
            cls.UI.MainWidget.setCurrentWidget(cls.UI.Translator)
        elif cls.mode == "Writing":
            cls.stop_camera()
            cls.mode = None
            cls.UI.MainWidget.setCurrentWidget(cls.UI.Translator)
        else:
            cls.stop_camera()
            cls.mode = None
            cls.UI.MainWidget.setCurrentWidget(cls.UI.Overview)

    @classmethod
    def start_camera(cls):
        cls.thread = VideoThread(0)  # Set the camera index as needed
        cls.thread.change_ImageSignal.connect(cls.update_image)
        cls.thread.prediction_ready.connect(cls.predictions_update)
        cls.thread.start()
        cls.UI.ToggleCamera.setText("Turn Camera Off")
        cls.UI.CameraStatus.setText("Press Start in order to start Typing")
        cls.camera_on = True

    @classmethod
    def predictions_update(cls,predictedword):
        cls.TypedWord = predictedword
        cls.UI.CameraStatus.setText("Camera Ready, Press add to save word, otherwise, press Continue")
        cls.UI.LiveContinueButton.setText("Continue")
        cls.UI.predictionlabel.setText(cls.TypedWord)


    @classmethod
    def pushtoType(cls):
        if cls.TypedWord !=None:
            print("Typing")
            typedtext = cls.UI.typedinputlabel.text()
            new_text = typedtext + cls.TypedWord
            print(new_text)
            cls.UI.typedinputlabel.setText(new_text)
            cls.TypedWord = None

    @classmethod
    def stop_camera(cls):
        if cls.thread and cls.thread.isRunning():
            cls.thread.stop()
            cls.thread.wait()
        cls.camera_on = False
        cls.UI.CameraStatus.setText("Turn the Camera On to proceed")
        cls.UI.ToggleCamera.setText("Turn Camera On")

    @classmethod
    def closeEvent(cls, event):
        cls.stop_camera()
        event.accept()

    @classmethod
    def ready_Up(cls):
        if cls.camera_on:
            cls.thread.start_collecting_frames() 
            cls.UI.CameraStatus.setText("Collecting Frames...")
        else:
            notificationhandler.trigger_notification(("Turn On or Select a Camera to start"),0,"info")
            cls.UI.ExpandableSideMenu.expandMenu()
            cls.UI.OptionsWidget.setCurrentWidget(self.ui.SettingsPage)


class SpellingBee(LiveInterface):

    @classmethod
    def initialise_mode(self,word):
        print("Bee")
        self.UI.LiveLabel.setText("Spelling Bee\nWord:")
        self.UI.CurrentWordLabel.setText(word)
        self.UI.LiveContinueButton.setText("Start")
        self.UI.LiveModeLabel.setText("SpellingBee")
        self.set_mode("Bee")


class WritingLive(LiveInterface):

    @classmethod
    def initialise_mode(self):
        print("Writing")
        self.UI.LiveLabel.setText("")
        self.UI.typedinfolabel.setText("Typed")
        self.UI.typedinputlabel.setText("")
        self.UI.LiveContinueButton.setText("Start")
        self.UI.LiveModeLabel.setText("Writing")
        self.set_mode("Writing")

class WordLive(LiveInterface):
    word_instance = None

    @classmethod
    def set_word(self,word):
        self.word_instance = word
        
    @classmethod
    def initialise_mode(self):
        print("Word")
        self.UI.LiveLabel.setText("Word:")
        self.UI.CurrentWordLabel.setText(self.word_instance.name)
        self.UI.LiveContinueButton.setText("Start")
        self.UI.LiveModeLabel.setText(self.word_instance.name)
        self.set_mode("Word")