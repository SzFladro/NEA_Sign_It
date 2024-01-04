import os
import cv2
import json
import numpy as np
from tqdm import tqdm
import mediapipe as mp
from sklearn.preprocessing import OneHotEncoder
import random

class VideoDataPreprocessor:
    def __init__(self, data_dir, output_dir, class_mapping_file='class_mapping.json'):
        self.data_dir = data_dir
        self.output_dir = output_dir
        self.class_mapping_file = class_mapping_file
        self.class_mapping = {}

    def preprocess_data(self, num_frames=20, frame_interval=2, num_augmentations=3, noise_factor=0.1):
        for class_name in tqdm(os.listdir(self.data_dir), desc="Processing Classes"):
            class_path = os.path.join(self.data_dir, class_name)

            if os.path.isdir(class_path):
                # Update class mapping
                if class_name not in self.class_mapping:
                    self.class_mapping[class_name] = len(self.class_mapping)

                # Load videos from the class folder
                videos = [video for video in os.listdir(class_path)]

                # Initialize data and labels for the class
                class_data = np.empty((0, 20, 126), dtype=np.float32)

                for video in tqdm(videos, desc=f"Processing {class_name} Videos", leave=False):
                    video_path = os.path.join(class_path, video)
                    class_data = self._process_video(class_name, video_path, num_frames, frame_interval, num_augmentations, noise_factor, class_data)

                if class_data is not None:
                    self.save_class_data(class_name, class_data)

    def _process_video(self, class_name, video_path, num_frames, frame_interval, num_augmentations, noise_factor, class_data):
        mp_holistic = mp.solutions.holistic

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"Error opening video: {video_path}")
            return None

        original_frames = []  # Store the original 20 frames
        augmented_frames = []  # Store the augmented frames

        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            noise_frames = np.random.normal(0, 1, (int(cap.get(cv2.CAP_PROP_FRAME_COUNT)), *cap.read()[1].shape)).astype('uint8')

            i = 0
            while i < num_frames:
                ret, frame = cap.read()

                if not ret:
                    break

                frame = cv2.flip(frame, 1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Extract keypoints for the frame before applying noise
                results = holistic.process(rgb_frame)
                landmarks = self._extract_keypoints(results)
                original_frames.append(landmarks)

                # Apply noise to every frame
                noisy_frame = cv2.addWeighted(rgb_frame, 1 - noise_factor, noise_frames[i], noise_factor, 0)

                # Augment frames directly to meet the required number of frames and augmentations
                for _ in range(num_augmentations):
                    augmented_frame = noisy_frame.copy()
                    if random.choice([True, False]):
                        # Resize
                        augmented_frame = cv2.resize(augmented_frame, (int(noisy_frame.shape[1] * random.uniform(0.8, 1.2)),
                                                                           int(noisy_frame.shape[0] * random.uniform(0.8, 1.2))))
                    else:
                        # Rotate
                        augmented_frame = cv2.rotate(augmented_frame, random.choice([cv2.ROTATE_90_CLOCKWISE, cv2.ROTATE_90_COUNTERCLOCKWISE]))

                    augmented_results = holistic.process(augmented_frame)
                    augmented_landmarks = self._extract_keypoints(augmented_results)
                    augmented_frames.append(augmented_landmarks)

                # Increment counter for frame extraction
                i += 1

        cap.release()
        cv2.destroyAllWindows()

        # Repeat the last frame until the 20-frame requirement is satisfied for both original and augmented frames
        while len(original_frames) < num_frames:
            original_frames.append(original_frames[-1].copy())

        while len(augmented_frames) < num_frames * num_augmentations:
            augmented_frames.append(augmented_frames[-1].copy())

        # Stack the original and augmented frames
        original_frames_array = np.array(original_frames)
        augmented_frames_array = np.array(augmented_frames)
        stacked_frames = np.vstack([original_frames_array[np.newaxis, ...], augmented_frames_array])

        # Add the data for this video to class_data
        class_data = np.append(class_data, stacked_frames[np.newaxis, ...], axis=0)
        print(class_data.shape)

        return class_data

    def _extract_keypoints(self, results):
        lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
        rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
        return np.concatenate([lh, rh]) 

    def save_class_data(self, class_name, class_data):
        numerical_label = self.class_mapping[class_name]
        encoder = OneHotEncoder(categories='auto', sparse=False)
        one_hot_label = encoder.fit_transform([[numerical_label]])

        class_output_dir = os.path.join(self.output_dir, class_name)
        os.makedirs(class_output_dir, exist_ok=True)

        np.save(os.path.join(class_output_dir, 'hand_landmarks.npy'), class_data, allow_pickle=True)
        np.save(os.path.join(class_output_dir, 'label.npy'), one_hot_label, allow_pickle=True)

    def save_class_mapping(self):
        with open(self.class_mapping_file, 'w') as f:
            json.dump(self.class_mapping, f)

    def shutdown(self):
        os.system("shutdown /s /t 1")

if __name__ == "__main__":
    home_directory = os.path.expanduser("~")
    input_directory = os.path.join(home_directory, 'Videos', 'Final')
    output_directory = os.path.join(home_directory, 'Videos', 'Train_2')
    data_preprocessor = VideoDataPreprocessor(data_dir=input_directory, output_dir=output_directory)
    data_preprocessor.preprocess_data(num_frames=20, frame_interval=2, num_augmentations=3, noise_factor=0.1)
    data_preprocessor.save_class_mapping()
    data_preprocessor.shutdown()
