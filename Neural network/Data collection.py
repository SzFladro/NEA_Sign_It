import os
import cv2
import json
import numpy as np
import mediapipe as mp
from sklearn.preprocessing import OneHotEncoder
import argparse
import string 

'''
Method which opens the camera, 
locates the hands/face/body(pose) and marks them collecting the coordinates and storing them within a numpy array containing all the coordinates from all the videos within a class.
'''
class VideoDataPreprocessor:
    OUTPUTDIR = os.path.join(os.path.expanduser("~"), 'Videos', 'Train_1')

    ##method that initialises the class local variables
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

    ##method for processing frames and locating the hands,face,pose from the image
    def mediapipe_detection(self,image, model):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
        image.flags.writeable = False                  # locks the image so that it isnt writable
        results = model.process(image)                 # Make prediction
        image.flags.writeable = True                   # unlocks the image to allow for connections to be drawn on 
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
        return image, results

    ##method for drawing the different connections to the frame using the coordinates of the different parts collected (landmarks)
    def draw_styled_landmarks(self,frame, results,holisticModel ):
        mp_drawer = mp.solutions.drawing_utils # Drawing utilities

        # Draw face connections
        mp_drawing.draw_landmarks(frame, results.face_landmarks, holisticModel.FACEMESH_TESSELATION, 
                                 mp_drawer.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1), 
                                 mp_drawer.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)) 
        # Draw pose connections
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, holisticModel.POSE_CONNECTIONS,
                                 mp_drawer.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4), 
                                 mp_drawer.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)) 
        # Draw left hand connections
        mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, holisticModel.HAND_CONNECTIONS, 
                                 mp_drawer.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4), 
                                 mp_drawer.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)) 
        # Draw right hand connections  
        mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, holisticModel.HAND_CONNECTIONS, 
                                 mp_drawer.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4), 
                                 mp_drawer.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)) 
        
    ##method for collecting seperating the different coordinates into their respective groups and storing it as an array
    def extract_keypoints(self,results):
        pose = np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
        face = np.array([[landmark.x, landmark.y, landmark.z] for landmark in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(468*3)
        lefthand = np.array([[landmark.x, landmark.y, landmark.z] for landmark in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
        righthand = np.array([[landmark.x, landmark.y, landmark.z] for landmark in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
        return np.concatenate([pose, face, lefthand, righthand])

    def preprocess_data(self,class_list):
        holisticModel = mp.solutions.holistic  
        cap = cv2.VideoCapture(0)
        args = self.get_args()
        detection_confidence = args.min_detection_confidence
        tracking_confidence = args.min_tracking_confidence
        NoVideos = args.Novideos
        NoFrames = args.frames
        Shape = args.shape

        with holisticModel.Holistic(min_detection_confidence=detection_confidence, min_tracking_confidence= tracking_confidence) as holistic:
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
                
                            if frame_num == 0: 
                                cv2.putText(image, 'Collecting First Frame', (120,200), 
                                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 4, cv2.LINE_AA)
                                cv2.putText(image, 'Collecting frames for class {}, Video Number {}'.format(class_name, VidNo), (15,12), 
                                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                                # Show to screen
                                cv2.imshow('Collecting Data', image)
                                cv2.waitKey(500)
                            else: 
                                cv2.putText(image, 'Collecting frames for class {}, Video Number {}'.format(class_name, VidNo), (15,12), 
                                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                                # Show to screen
                                cv2.imshow('Collecting Data', image)
                
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
    
    '''
    adds the class names into dictioanaries
    '''
    def set_class_mapping(self, class_list):
        self.class_mapping = {class_name: i for i, class_name in enumerate(class_list)}
    
    '''
    method for saving the one hot encoded label along with the corresponding data into numpy files
    '''
    def save_class_data(self, class_name, class_data):
        numerical_label = self.class_mapping[class_name]
        one_hot_label = np.zeros(len(self.class_mapping), dtype=int)
        one_hot_label[numerical_label] = 1
        class_output_dir = os.path.join(self.output_dir, class_name)
        os.makedirs(class_output_dir, exist_ok=True)
        np.save(os.path.join(class_output_dir, 'hand_landmarks.npy'), class_data, allow_pickle=True)
        np.save(os.path.join(class_output_dir, 'label.npy'), one_hot_label, allow_pickle=True)

    ##method that saves all the labels {equilavent to the class name so eg. A} alongside their numerical value in dictionary to allow for one hot encoding
    def save_class_mapping(self, output_dir):
        mapfiledir = os.path.join(output_dir, self.class_mapping_file)
        with open(mapfiledir, 'w') as f:
            json.dump(self.class_mapping, f)

if __name__ == "__main__":
    class_list= list(string.ascii_uppercase)
    PrepareData = VideoDataPreprocessor()
    PrepareData.set_class_mapping(class_list)
    PrepareData.preprocess_data(class_list)



