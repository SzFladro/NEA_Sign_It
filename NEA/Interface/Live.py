from PySide6.QtCore import (QCoreApplication, QUrl, Qt, QThread, Signal, Slot)
from PySide6.QtGui import (QIcon, QImage,QPixmap)
from PySide6.QtMultimedia import QMediaDevices
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
import string
import time

from DataBase import config, SQLQueries
from Interface import Notifications, OverviewInterface

config_cam = config.Config()
camerainput = config_cam.get_main_camera()
model = tf.keras.models.load_model(u'Translator/BSLmodel.h5')
model.load_weights(u'Translator/BSLweights.h5')
mp_holistic = mp.solutions.holistic # Holistic model
mp_drawing = mp.solutions.drawing_utils # Drawing utilities

notificationhandler = Notifications.NotificationHandler

#define signs and currently available words
signs = list(string.ascii_uppercase)
AvailableWords = np.array(signs)

'''
    Thread class for real-time webcam processing and UI updates

    Attributes:
        change_ImageSignal (Signal): Signal for updating the main window with processed webcam frames
        frames_ready (Signal): Signal that permits the thread to capture 30 frames which are then ran through the neural network only when the Start button is pressed
        prediction_ready (Siganl): Signal which transferred the neural networks prediction back to the main thread allowing the UI to be updated
'''
class VideoThread(QThread):
    change_ImageSignal = Signal(np.ndarray)
    frames_ready = Signal(list)
    prediction_ready = Signal(str)

    '''
        Initialises the VideoThread instance

        Parameters:
            camera_index (int): Index of the camera to use
    '''
    def __init__(self, camera_index):
        super().__init__()
        self._run = False
        self.camera_index = camera_index
        self.frames =[]
        self.collect_frames = False

    '''
        Method which continually processes webcam frames, detects landmarks and updates UI
    '''
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

    #Stops the thread from updating the label with webcam frames, waits for it to fully stop
    def stop(self):
        self._run = False
        self.wait()

    #method that ensures that frames are only captured after the user presses the Start button
    def start_collecting_frames(self):
        self.collect_frames = True

    '''
        method which processes frames, locating the hands, face, body in the image
        It extracts coordinates of the features (x,y,z) 
        where
             x - horizontal position originating from the leftmost side of the image
             y - vertical position originating from the top of the image
             z - landmark depth originating from the midpoint of the hips, smaller value, closer landmark is to camera

        Return:
            results (tuple): storing the coordinates of all the different features
            image (NumPy array): representing the frame in BGR format
    '''
    def mediapipe_detection(self,image, model):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
        image.flags.writeable = False                  
        results = model.process(image)                 
        image.flags.writeable = True                    
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) 
        return image, results

    
    '''
        method which draws the landmarks and lines connecting them within the image outlining the users pose
        It does this for the face, body, left and right hand

        Parameters:
            frame (numPy array): represting the current frame in BGR format
            results (tuple): coordinates of all the features to be mapped on image
    '''
    def draw_styled_landmarks(self,frame, results):
        mp_drawing.draw_landmarks(frame, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION, 
                                 mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1), 
                                 mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)) 

        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4), 
                                 mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)) 

        mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4), 
                                 mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)) 

        mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4), 
                                 mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)) 
        
    '''
        method which separates the different coordinates into their respective groups storing them as an array

        Parameters:
            results (tuple): coordinates of all the features to be mapped on image

        Return:
            numPy array: the extracted keypoints
    '''
    def extract_keypoints(self,results):
        pose = np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
        face = np.array([[landmark.x, landmark.y, landmark.z] for landmark in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(468*3)
        lefthand = np.array([[landmark.x, landmark.y, landmark.z] for landmark in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
        righthand = np.array([[landmark.x, landmark.y, landmark.z] for landmark in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
        return np.concatenate([pose, face, lefthand, righthand])

'''
    Class to manage application modes, allowing the correct return button function to be assigned for the coresponding live screens: Writing, Word or Spelling Bee

    Attributes:
        mode (str or None): current application mode
'''
class ModeManager:
    mode = None

    #method to set the current application mode 
    @classmethod
    def set_mode(cls,new_mode):
        cls.mode = new_mode

    #method to get the current application mode
    @classmethod
    def get_mode(cls):
        return cls.mode

'''
    Class for managing the UI and the webcam
    
    Attributes:
        UI (object): Reference to the main window instance
        camera_on (bool): Indicates whether the camera is currently in use
        thread (VideoThread): Thread for real_time webcam processing
        TypedWord (str): the word predicted by the model
'''
class LiveInterface:
    UI = None
    camera_on = False
    thread = None
    TypedWord = None

    '''
        Sets the application mode using ModeManager

        Parameters:
            Livemode (Str): application mode to be set (eg.: "Bee", "Writing", "Word")
    '''
    @classmethod
    def set_mode(self,Livemode):
        ModeManager.set_mode(Livemode)

    '''
        Retrieves current application mode

        Return:
            mode (Str): application mode from ModeManager
    '''
    @classmethod
    def get_mode(self):
        return ModeManager.get_mode()

    '''
        Sets the UI instance and initialise UI-related attributes, adds listeners once throughout runtime for this section of UI

        Parameters:
            ui_instance (object): Reference to the main window instance
    '''
    @classmethod
    def set_ui(self, ui_instance):
        self.UI = ui_instance
        self.frame_width = self.UI.LiveCVframe.width()
        self.frame_height = self.UI.LiveCVframe.height()
        self.Live_Controls()

    #Connects listeners to the corresponding functions
    @classmethod
    def Live_Controls(self):
        self.UI.ToggleCamera.clicked.connect(lambda: self.CameraControls())
        self.UI.LiveContinueButton.clicked.connect(lambda:self.ready_Up())
        self.UI.LiveAddtoTypedButton.clicked.connect(lambda: self.pushtoType())
        self.UI.LiveToTranslatorButton.clicked.connect(lambda: self.returnbacktoUI())
        self.UI.removetypedButton.clicked.connect(lambda:self.remove_typed())

    #Clears text from the typedinputlabel within the UI
    @classmethod
    def remove_typed(self):
        self.UI.typedinputlabel.setText("")

    '''
        Updates the UI with the processed webcam image

        Parameters:
            cv_img (NumPy array): processed webcam image
    '''
    @classmethod
    def update_image(self, cv_img):
        if self.camera_on:
            qt_img = self.convert_cv_qt(cv_img)
            self.UI.LiveFootageLabel.setPixmap(qt_img)

    '''
        Converts a NumPy rray representing an image from OpenCV format to Qt so that it can be displayed as a PixMap within a label

        Parameters:
            cv_img (NumPy array): Image in OpenCV format

        Return: 
            QPixmap object representing the converted image in Qt format
    '''
    @classmethod
    def convert_cv_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        # Scales image to match the dimensions of the LiveCVframe
        scaled_image = convert_to_Qt_format.scaled(self.frame_width, self.frame_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
        return QPixmap.fromImage(scaled_image)

    #Turns the camera on/ off based on user's selection in UI
    @classmethod
    def CameraControls(self):
        if self.camera_on:
            self.stop_camera()
        else:
            self.start_camera()

    #returns the user back to the main UI based on the current application mode
    @classmethod
    def returnbacktoUI(self):
        self.stop_camera()
        mode = self.get_mode()
        if mode == "Bee":
            self.set_mode(None)
            self.UI.MainWidget.setCurrentWidget(self.UI.Translator)
        elif mode == "Writing":
            self.set_mode(None)
            self.UI.MainWidget.setCurrentWidget(self.UI.Translator)
        else:
            self.set_mode(None)
            OverviewInterface.InterfaceOverview.overviewInterface()

    '''
        Chooses the camera based on user's selection within the UI
        Handles notifications for camera-related issues

        Return:
            camera_index (int): index corresponding to selected camera within CameraSettingComboBox
    '''
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

    #Initiates the video thread for real-time webcam processing, updating UI accordingly
    @classmethod 
    def start_camera(self):
        camera_indexed = self.camera_chooser()
        if camera_indexed >= 0:
            self.thread = VideoThread(camera_indexed)  # Set the camera index as needed
            self.thread.change_ImageSignal.connect(self.update_image)
            self.thread.prediction_ready.connect(self.predictions_update)
            self.thread.start()
            self.UI.ToggleCamera.setText("Turn Camera Off")
            self.UI.CameraStatus.setText("Press Start in order to start Typing")
            self.camera_on = True
        else:
            self.UI.ExpandableSideMenu.expandMenu()
            self.UI.OptionsWidget.setCurrentWidget(self.UI.SettingsPage)

    '''
        Updates the predictionlabel with the predicted word and adjusts LiveContinueButton text within UI

        Parameters:
            predictedword (str): predicted word by the model from VideoThread
    '''
    @classmethod
    def predictions_update(self,predictedword):
        self.TypedWord = predictedword
        self.UI.CameraStatus.setText("Camera Ready, Press add to save word, otherwise, press Continue")
        self.UI.LiveContinueButton.setText("Continue")
        self.UI.predictionlabel.setText(self.TypedWord)

    #Appends the predicted word to the typedinputlabel when user presses button
    @classmethod
    def pushtoType(self):
        if self.TypedWord !=None:
            typedtext = self.UI.typedinputlabel.text()
            new_text = typedtext + self.TypedWord
            self.UI.typedinputlabel.setText(new_text)
            self.TypedWord = None

    #Stops the webcam processing thread, notifies user as well as turning the camera off
    @classmethod
    def stop_camera(self):
        if self.thread and self.thread.isRunning():
            self.thread.stop()
            self.thread.wait()
        self.camera_on = False
        self.UI.CameraStatus.setText("Turn the Camera On to proceed")
        self.UI.ToggleCamera.setText("Turn Camera On")
        return None

    '''
        Handles the close event of the application stopping frame collection in video thread,
        
        Parameters:
            event: close event triggered by the user
    '''
    @classmethod
    def closeEvent(self, event):
        self.stop_camera()
        event.accept()

    #initiates the webcam to start collecting frames for processing in video thread
    @classmethod
    def ready_Up(self):
        if self.camera_on:
            self.thread.start_collecting_frames() 
            self.UI.CameraStatus.setText("Collecting Frames...")
        else:
            notificationhandler.trigger_notification(("Turn On or Select a Camera to start"),0,"info")
            self.UI.ExpandableSideMenu.expandMenu()
            self.UI.OptionsWidget.setCurrentWidget(self.UI.SettingsPage)

    #initialises the current application mode, clearing and resetting this part of the UI
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

#Class for the spelling bee mode inheriting from LiveInterface
class SpellingBee(LiveInterface):
    '''
        Initialises UI labels for the Spelling Bee mode

        Parameters:
            word(str): the word entered to be spelt within the spelling be 
    '''
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

# Class for the Writing mode inheriting from LiveInterface
class WritingLive(LiveInterface):
    #Initialises UI labels for the Writing mode
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

'''
    Class for the Word mode inheriting from LiveInterface

    Attributes:
        word_instance (object): word instance corresponding to the word from the catalogue -> overview -> WordLive
'''
class WordLive(LiveInterface):
    word_instance = None

    #Sets the word instance for the mode
    @classmethod
    def set_word(self,word):
        self.word_instance = word
        
    #Logs user's attempt of the word within the database
    @classmethod
    def addattempt(self):
        username = config_cam.get_username()
        if username !=None:
            SQLQueries.AddAttempt(username,self.word_instance.name)
        else:
            notificationhandler.trigger_notification(("Create an account to save progress"),0,"info")
        return None

    #Initialises UI labels for the Word mode
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

