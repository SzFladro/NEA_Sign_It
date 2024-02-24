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


class VideoThread(QThread):
    change_ImageSignal = Signal(np.ndarray)
    mp_holistic = mp.solutions.holistic # Holistic model
    mp_drawing = mp.solutions.drawing_utils # Drawing utilities
    model = tf.keras.model.load_model("BSLmodel.h5")
    model.load_weights("BSLweights.h5")


    def __init__(self, camera_index):
        super.__init__()
        self._run = False
        self.camera_index = camera_index

    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--maxframecount", help='maximum video_frames', type=int, default=30)
        parser.add_argument("--min_detection_confidence", help='min_detection_confidence', type=float,
                            default=0.7)
        parser.add_argument("--min_tracking_confidence", help='min_tracking_confidence', type=float,
                            default=0.5)
        args = parser.parse_args()
        return args

    def run(self):
        args = self.get_args()
        cap = cv2.VideoCapture(self.camera_index)
        self._run = True
        frame_count =0
        frames = []
        framemaxcount = args.maxframecount
        try:
            while self._run:
                ret, cv_img = cap.read()
                if ret:
                    self.change_ImageSignal.emit(cv_img)
                    if frame_count < framemaxcount:
                        frames.append(cv_image.copy())
                        frame_count +=1
                    elif frame_count == framemaxcount:
                        self.process_frames(frames)
                else:
                    frame_count =0
        finally:
            cap.release()

    def stop(self):
        self._run = False
        self.wait()

    def mediapipe_detection(image, model):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR-CONVERSION BGR-to-RGB
        image.flags.writeable = False                  # Convert image to not-writeable
        results = model.process(image)                 # Make prediction
        image.flags.writeable = True                   # Convert image to writeable 
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR-COVERSION RGB-to-BGR
        return image, results

    def draw_styled_landmarks(image, results):
        # Draw face connections
        mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION, 
                                 mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1), 
                                 mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
                                 ) 
        # Draw pose connections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4), 
                                 mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                                 ) 
        # Draw left hand connections
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4), 
                                 mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                                 ) 
        # Draw right hand connections  
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4), 
                                 mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                 ) 

    def extract_keypoints(results):
        pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
        face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(468*3)
        lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
        rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
        return np.concatenate([pose, face, lh, rh])
