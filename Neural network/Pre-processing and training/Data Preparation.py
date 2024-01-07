import os
import cv2
import json
import numpy as np
from tqdm import tqdm
import mediapipe as mp
from sklearn.preprocessing import OneHotEncoder
import random
from concurrent.futures import ProcessPoolExecutor

class VideoDataPreprocessor:
    def __init__(self, data_dir, output_dir, class_mapping_file='class_mapping.json'):
        self.data_dir = data_dir
        self.output_dir = output_dir
        self.class_mapping_file = class_mapping_file
        self.class_mapping = {}

    def preprocess_data(self, num_frames=30, num_augmentations=6):
        max_workers = 4  
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for class_name in tqdm(os.listdir(self.data_dir), desc="Processing Classes"):
                class_path = os.path.join(self.data_dir, class_name)

                if os.path.isdir(class_path):
                    # Update class mapping
                    if class_name not in self.class_mapping:
                        self.class_mapping[class_name] = len(self.class_mapping)

                    # Load videos from the class folder
                    videos = [video for video in os.listdir(class_path)]

                    # Initialize data and labels for the class
                    class_data = np.empty((0, num_frames, 126), dtype=np.float32)

                    for video in tqdm(videos, desc=f"Processing {class_name} Videos", leave=False):
                        video_path = os.path.join(class_path, video)
                        futures.append(executor.submit(self._process_video, class_name, video_path, num_frames, num_augmentations, class_data))
                        print(class_data.shape)

            results = [future.result() for future in tqdm(futures, desc="Processing Videos", total=len(futures))]

            for class_name, video_data in zip(os.listdir(self.data_dir), results):
                if video_data is not None:
                    self.save_class_data(class_name, video_data)

    def rotate_frame(self, frame, angle):
        height, width = frame.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
        processed_frame = cv2.warpAffine(frame, rotation_matrix, (width, height), flags=cv2.INTER_LINEAR)
        return processed_frame

    def augment(self, frame, augment_counter, num_augmentations, operations, noise_factor):
        if len(operations) != num_augmentations:
            operations.append([np.random.normal(0, 1, frame.shape).astype('uint8'), 0])
            operations.append([0, random.randrange(-60, 60)])
            operations.append([np.random.normal(0, 1, frame.shape).astype('uint8'), random.randrange(-60, 60)])
        if augment_counter == 0:
            processed_frame = cv2.addWeighted(frame, 1 - noise_factor, operations[augment_counter][0], noise_factor, 0)
        elif augment_counter == 1:
            processed_frame = self.rotate_frame(frame, operations[augment_counter][1])
        else:
            noisy_frame = cv2.addWeighted(frame, 1 - noise_factor, operations[augment_counter][0], noise_factor, 0)
            processed_frame = self.rotate_frame(noisy_frame, operations[augment_counter][1])
        return processed_frame

    def _process_video(self, class_name, video_path, num_frames, num_augmentations, class_data):
        mp_holistic = mp.solutions.holistic
        noise_factor = 0.1
        cap = cv2.VideoCapture(video_path)

        original_landmarks = []  # Store the original 30 landmarks
        augmented_landmarks = np.empty((num_augmentations, num_frames, 126))

        operations = []

        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            frame_count = 0
            while frame_count < num_frames:
                ret, frame = cap.read()

                if not ret:
                    break

                frame = cv2.flip(frame, 1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Extract keypoints for the frame before applying noise
                results = holistic.process(rgb_frame)
                landmarks = self._extract_keypoints(results)
                original_landmarks.append(landmarks)
                for augment_counter in range(num_augmentations):
                    processed_frame_landmarked = self.augment(rgb_frame, augment_counter, num_augmentations, operations, noise_factor)
                    results = holistic.process(processed_frame_landmarked)
                    augmented_landmarks[augment_counter, frame_count, :] = self._extract_keypoints(results)

                # Increment counter for frame extraction
                frame_count += 1

        cap.release()
        cv2.destroyAllWindows()
        # Repeat the last frame until the 30-frame requirement is satisfied for both original and augmented frames
        while len(original_landmarks) < num_frames:
            original_landmarks.append(original_landmarks[-1].copy())

        original_landmarks = np.array(original_landmarks)
        # Add the data for this video to class_data
        class_data = np.append(class_data, original_landmarks[np.newaxis, ...], axis=0)
        class_data = np.append(class_data, augmented_landmarks, axis=0)
        
        return class_name, class_data

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
        print(class_data.shape)
        np.save(os.path.join(class_output_dir, 'hand_landmarks.npy'), class_data, allow_pickle=True)
        np.save(os.path.join(class_output_dir, 'label.npy'), one_hot_label, allow_pickle=True)

    def save_class_mapping(self, output_directory):
        mapfiledir = os.path.join(output_directory, self.class_mapping_file)
        with open(mapfiledir, 'w') as f:
            json.dump(self.class_mapping, f)

    def shutdown(self):
        os.system("shutdown /s /t 1")

if __name__ == "__main__":
    home_directory = os.path.expanduser("~")
    input_directory = os.path.join(home_directory, 'Videos', 'Final')
    output_directory = os.path.join(home_directory, 'Videos', 'Train_2')
    data_preprocessor = VideoDataPreprocessor(data_dir=input_directory, output_dir=output_directory)
    data_preprocessor.preprocess_data(num_frames=30, num_augmentations=6)
    data_preprocessor.save_class_mapping(output_directory)
    data_preprocessor.shutdown() 