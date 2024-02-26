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
from PySide6.QtMultimedia import QMediaDevices
import cv2
import numpy as np
import os
import time
import mediapipe as mp
import string
import tensorflow as tf
import bcrypt
import hashlib
import hmac
import re


from DataBase import config, SQLQueries
from Interface import Notifications, OverviewInterface

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
    mode = None

    @classmethod
    def set_mode(self,Livemode):
        self.mode = Livemode

    @classmethod
    def set_ui(self, ui_instance):
        self.UI = ui_instance
        self.frame_width = self.UI.LiveCVframe.width()
        self.frame_height = self.UI.LiveCVframe.height()
        self.Live_Controls()

    @classmethod
    def Live_Controls(self):
        self.UI.ToggleCamera.clicked.connect(lambda: self.CameraControls())
        self.UI.LiveContinueButton.clicked.connect(lambda:self.ready_Up())
        self.UI.LiveAddtoTypedButton.clicked.connect(lambda: self.pushtoType())
        self.UI.LiveToTranslatorButton.clicked.connect(lambda: self.returnbacktoUI())
        self.UI.removetypedButton.clicked.connect(lambda:self.remove_typed())

    @classmethod
    def remove_typed(self):
        self.UI.typedinputlabel.setText("")

    @classmethod
    def update_image(self, cv_img):
        if self.camera_on:
            qt_img = self.convert_cv_qt(cv_img)
            self.UI.LiveFootageLabel.setPixmap(qt_img)

    @classmethod
    def convert_cv_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        # Scales image to match the dimensions of the LiveCVframe
        scaled_image = convert_to_Qt_format.scaled(self.frame_width, self.frame_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
        return QPixmap.fromImage(scaled_image)

    @classmethod
    def CameraControls(self):
        if self.camera_on:
            self.stop_camera()
        else:
            self.start_camera()

    @classmethod
    def returnbacktoUI(self):
        self.stop_camera()
        if self.mode == "Bee":
            self.mode = None
            self.UI.MainWidget.setCurrentWidget(self.UI.Translator)
        elif self.mode == "Writing":
            self.mode = None
            self.UI.MainWidget.setCurrentWidget(self.UI.Translator)
        else:
            self.mode = None
            OverviewInterface.InterfaceOverview.overviewInterface()


    @classmethod
    def camera_chooser(self):
        selected_camera = self.UI.CameraSettingComboBox.currentText()
        available_cameras= QMediaDevices.videoInputs()
        if available_cameras:
            for cameras in available_cameras:
                if cameras.description() == selected_camera:
                    camera_index = self.UI.CameraSettingComboBox.currentIndex()-1
                    return camera_index
                else:
                    notificationhandler.trigger_notification(("Selected Camera seems to be offline\n Defaulting to default camera"),0,"info")
                    return 0   
        else:
            notificationhandler.trigger_notification(("No Camera found"),0,"info")
            return -1


            

    @classmethod
    def start_camera(self):
        camera_indexed = self.camera_chooser()
        if camera_indexed >= 0:
            self.thread = VideoThread(0)  # Set the camera index as needed
            self.thread.change_ImageSignal.connect(self.update_image)
            self.thread.prediction_ready.connect(self.predictions_update)
            self.thread.start()
            self.UI.ToggleCamera.setText("Turn Camera Off")
            self.UI.CameraStatus.setText("Press Start in order to start Typing")
            self.camera_on = True
        else:
            self.UI.ExpandableSideMenu.expandMenu()
            self.UI.OptionsWidget.setCurrentWidget(self.ui.SettingsPage)

    @classmethod
    def predictions_update(self,predictedword):
        self.TypedWord = predictedword
        self.UI.CameraStatus.setText("Camera Ready, Press add to save word, otherwise, press Continue")
        self.UI.LiveContinueButton.setText("Continue")
        self.UI.predictionlabel.setText(self.TypedWord)


    @classmethod
    def pushtoType(self):
        if self.TypedWord !=None:
            typedtext = self.UI.typedinputlabel.text()
            new_text = typedtext + self.TypedWord
            self.UI.typedinputlabel.setText(new_text)
            self.TypedWord = None

    @classmethod
    def stop_camera(self):
        if self.thread and self.thread.isRunning():
            self.thread.stop()
            self.thread.wait()
        self.camera_on = False
        self.UI.CameraStatus.setText("Turn the Camera On to proceed")
        self.UI.ToggleCamera.setText("Turn Camera On")
        return None

    @classmethod
    def closeEvent(self, event):
        self.stop_camera()
        event.accept()

    @classmethod
    def ready_Up(self):
        if self.camera_on:
            self.thread.start_collecting_frames() 
            self.UI.CameraStatus.setText("Collecting Frames...")
        else:
            notificationhandler.trigger_notification(("Turn On or Select a Camera to start"),0,"info")
            self.UI.ExpandableSideMenu.expandMenu()
            self.UI.OptionsWidget.setCurrentWidget(self.ui.SettingsPage)

    @classmethod
    def initialise_mode(self):
        self.UI.LiveModeLabel.setText("")
        self.UI.LiveToTranslatorButton.setText("")
        self.UI.typedinputlabel.setText("")
        self.UI.LiveLabel.setText("")
        self.UI.CurrentWordLabel.setText("")
        self.UI.LiveContinueButton.setText("Start")
        self.UI.predictionlabel.setText("")
        self.stop_camera()


class SpellingBee(LiveInterface):

    @classmethod
    def initialise_mode(self,word):
        self.stop_camera()
        self.UI.LiveModeLabel.setText("SpellingBee")
        self.UI.LiveToTranslatorButton.setText("Back to Translator")
        self.UI.typedinputlabel.setText("")
        self.UI.LiveLabel.setText("Word:")
        self.UI.CurrentWordLabel.setText(word)
        self.UI.LiveContinueButton.setText("Start")
        self.UI.predictionlabel.setText("")
        self.set_mode("Bee")

class WritingLive(LiveInterface):

    @classmethod
    def initialise_mode(self):
        self.stop_camera()
        self.UI.LiveModeLabel.setText("Writing")
        self.UI.LiveToTranslatorButton.setText("Back to Translator")
        self.UI.typedinputlabel.setText("")
        self.UI.LiveLabel.setText("")
        self.UI.CurrentWordLabel.setText("")
        self.UI.LiveContinueButton.setText("Start")
        self.UI.predictionlabel.setText("")        
        self.set_mode("Writing")


class WordLive(LiveInterface):
    word_instance = None

    @classmethod
    def set_word(self,word):
        self.word_instance = word
        
    @classmethod
    def addattempt(self):
        username = config.get_username()
        if username !=None:
            SQLQueries.AddAttempt(username,self.word_instance)
        else:
            notificationhandler.trigger_notification(("Create an account to save progress"),0,"info")
        return None

    @classmethod
    def initialise_mode(self):
        self.UI.LiveModeLabel.setText(self.word_instance.name)
        self.UI.LiveToTranslatorButton.setText(f"Back to {self.word_instance.name} Overview")
        self.UI.typedinputlabel.setText("")
        self.UI.LiveLabel.setText("Word:")
        self.UI.CurrentWordLabel.setText(self.word_instance.name)
        self.UI.LiveContinueButton.setText("Start")
        self.UI.predictionlabel.setText("")
        self.addattempt()
        self.stop_camera()
        self.set_mode("Word")

