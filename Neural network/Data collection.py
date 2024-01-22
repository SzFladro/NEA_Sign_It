import os
import cv2
import json
import numpy as np
from tqdm import tqdm
import mediapipe as mp
from sklearn.preprocessing import OneHotEncoder
import random
import argparse
import string 

class VideoDataPreprocessor:
    OUTPUTDIR = os.path.join(os.path.expanduser("~"), 'Videos', 'Train_1')

    def __init__(self,  class_mapping_file='class_mapping.json'):
        self.output_dir = self.OUTPUTDIR
        self.class_mapping_file = class_mapping_file
        self.class_mapping = {}
        self.args = self.get_args()

    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--shape", help='shape of array', type=int, default=1662)
        parser.add_argument("--Novideos", help='number of videos per class', type=int, default=90)
        parser.add_argument("--frames", help='video_frames', type=int, default=30)
        parser.add_argument("--min_detection_confidence", help='min_detection_confidence', type=float,
                            default=0.7)
        parser.add_argument("--min_tracking_confidence", help='min_tracking_confidence', type=float,
                            default=0.5)
 

        args = parser.parse_args()
        return args

    def mediapipe_detection(self,image, model):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
        image.flags.writeable = False                  # Image is no longer writeable
        results = model.process(image)                 # Make prediction
        image.flags.writeable = True                   # Image is now writeable 
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
        return image, results

    def draw_styled_landmarks(self,image, results,mp_holistic ):
        mp_drawing = mp.solutions.drawing_utils # Drawing utilities

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
    def extract_keypoints(self,results):
        pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
        face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(468*3)
        lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
        rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
        return np.concatenate([pose, face, lh, rh])

    def preprocess_data(self,class_list):
        mp_holistic = mp.solutions.holistic  # Holistic model
        cap = cv2.VideoCapture(0)
        args = self.get_args()
        detection_confidence = args.min_detection_confidence
        tracking_confidence = args.min_tracking_confidence
        NoVideos = args.Novideos
        NoFrames = args.frames
        Shape = args.shape

        start_index = class_list.index('Z')
        class_list = class_list[start_index:]

        with mp_holistic.Holistic(min_detection_confidence=detection_confidence, min_tracking_confidence= tracking_confidence) as holistic:
            while cap.isOpened():

                for class_name in class_list:
                    class_data = np.empty((0, NoFrames, Shape), dtype=np.float32)
                    Vidlandmarks = np.empty((NoVideos, NoFrames, Shape), dtype=np.float32)

                    for VidNo in range(NoVideos):
                        for frame_num in range(NoFrames):

                            ret, frame = cap.read()

                            # Make detections
                            image, results = self.mediapipe_detection(frame, holistic)

                            # Draw landmarks
                            self.draw_styled_landmarks(image, results,mp_holistic )
                
                            # NEW Apply wait logic
                            if frame_num == 0: 
                                cv2.putText(image, 'STARTING COLLECTION', (120,200), 
                                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 4, cv2.LINE_AA)
                                cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(class_name, VidNo), (15,12), 
                                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                                # Show to screen
                                cv2.imshow('OpenCV Feed', image)
                                cv2.waitKey(500)
                            else: 
                                cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(class_name, VidNo), (15,12), 
                                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                                # Show to screen
                                cv2.imshow('OpenCV Feed', image)
                
                            keypoints = self.extract_keypoints(results)
                            print(keypoints)
                            Vidlandmarks[VidNo, frame_num, :] = keypoints
                            # Break 
                            if cv2.waitKey(10) & 0xFF == ord('q'):
                                break
                    class_data= np.concatenate([class_data,Vidlandmarks],axis=0)
                    self.save_class_data(class_name, class_data)
                                        
                cap.release()
                cv2.destroyAllWindows()
                self.save_class_mapping(self.output_dir)

    def set_class_mapping(self, class_list):
        self.class_mapping = {class_name: i for i, class_name in enumerate(class_list)}
     
    def save_class_data(self, class_name, class_data):
        numerical_label = self.class_mapping[class_name]
        one_hot_label = np.zeros(len(self.class_mapping), dtype=int)
        one_hot_label[numerical_label] = 1
        class_output_dir = os.path.join(self.output_dir, class_name)
        os.makedirs(class_output_dir, exist_ok=True)
        np.save(os.path.join(class_output_dir, 'hand_landmarks.npy'), class_data, allow_pickle=True)
        np.save(os.path.join(class_output_dir, 'label.npy'), one_hot_label, allow_pickle=True)


    def save_class_mapping(self, output_dir):
        mapfiledir = os.path.join(output_dir, self.class_mapping_file)
        with open(mapfiledir, 'w') as f:
            json.dump(self.class_mapping, f)

##stopped code at M
if __name__ == "__main__":
    class_list= list(string.ascii_uppercase)
    PrepareData = VideoDataPreprocessor()
    PrepareData.set_class_mapping(class_list)
    PrepareData.preprocess_data(class_list)



