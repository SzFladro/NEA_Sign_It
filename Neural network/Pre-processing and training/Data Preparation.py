import os
import cv2
import json
import numpy as np
from tqdm import tqdm
import mediapipe as mp
from sklearn.preprocessing import OneHotEncoder
import random
import argparse

class VideoDataPreprocessor:
    HEIGHT = 500
    WIDTH = 500
    SHAPE = 126
    MIN_DETECTION_CONFIDENCE = 0.5
    MIN_TRACKING_CONFIDENCE = 0.5
    NOISE_FACTOR = 0.05

    def __init__(self, data_dir, output_dir, class_mapping_file='class_mapping.json'):
        self.data_dir = data_dir
        self.output_dir = output_dir
        self.class_mapping_file = class_mapping_file
        self.class_mapping = {}
        self.args = self.get_args()

        self.rotation_matrix = cv2.getRotationMatrix2D((self.WIDTH / 2, self.HEIGHT / 2), 0, 1)

    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--height", help='image_height', type=int, default=self.HEIGHT)
        parser.add_argument("--width", help='image_width', type=int, default=self.WIDTH)
        parser.add_argument("--shapes", help='shape of array', type=int, default=self.SHAPE)
        parser.add_argument("--min_detection_confidence", help='min_detection_confidence', type=float,
                            default=self.MIN_DETECTION_CONFIDENCE)
        parser.add_argument("--min_tracking_confidence", help='min_tracking_confidence', type=float,
                            default=self.MIN_TRACKING_CONFIDENCE)
        parser.add_argument("--noise_factor", help='noise_factor', type=float, default=self.NOISE_FACTOR)

        args = parser.parse_args()
        return args

    def preprocess_data(self, num_frames, num_augmentations):
        for class_name in tqdm(os.scandir(self.data_dir), desc="Processing Classes"):
            if class_name.is_dir():
                # Update class mapping
                if class_name.name not in self.class_mapping:
                    self.class_mapping[class_name.name] = len(self.class_mapping)

                # Load videos from the class folder
                videos = [video.name for video in os.scandir(class_name.path) if video.is_file()]

                # Initialize data and labels for the class
                class_data = np.empty((0, num_frames, self.args.shapes), dtype=np.float32)

                for video in tqdm(videos, desc=f"Processing {class_name.name} Videos", leave=False):
                    video_path = os.path.join(class_name.path, video)
                    class_data = self._process_video(class_name.name, video_path, num_frames, num_augmentations, class_data)

                if class_data is not None:
                    self.save_class_data(class_name.name, class_data)

    def rotate_frame(self, frame, angle):
        processed_frame = cv2.warpAffine(frame, self.rotation_matrix, (self.WIDTH, self.HEIGHT), flags=cv2.INTER_LINEAR)
        return processed_frame

    def augment(self, frame, augment_counter, num_augmentations, operations, noise_factor):
        if len(operations) != num_augmentations:
            operations.append([np.random.normal(0, 1, frame.shape).astype('uint8'), 0])
            operations.append([np.random.normal(0, 1, frame.shape).astype('uint8'), random.randrange(-60, 60)])
            operations.append([0, random.randrange(0, 15)])
            while len(operations) != num_augmentations:
                operations.append([0, random.randrange(-30, 30)])

        if augment_counter == 0:
            processed_frame = cv2.addWeighted(frame, 1 - noise_factor, operations[augment_counter][0], noise_factor, 0)
        elif augment_counter == 1:
            noisy_frame = cv2.addWeighted(frame, 1 - noise_factor, operations[augment_counter][0], noise_factor, 0)
            processed_frame = self.rotate_frame(noisy_frame, operations[augment_counter][1])
        else:
            processed_frame = self.rotate_frame(frame, operations[augment_counter][1])
        return processed_frame

    def _process_video(self, class_name, video_path, num_frames, num_augmentations, class_data):
        mp_holistic = mp.solutions.holistic  # Holistic model
        cap = cv2.VideoCapture(video_path)

        original_landmarks = []  # Store the original 30 landmarks
        augmented_landmarks = np.empty((num_augmentations, num_frames, self.args.shapes))

        operations = []

        min_detection_confidence = self.args.min_detection_confidence
        min_tracking_confidence = self.args.min_tracking_confidence
        noise_factor = self.args.noise_factor

        with mp_holistic.Holistic(min_detection_confidence=min_detection_confidence,
                                  min_tracking_confidence=min_tracking_confidence) as holistic:
            frame_count = 0
            while frame_count < num_frames:
                ret, frame = cap.read()

                if not ret:
                    break

                frame = cv2.flip(frame, 1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rgb_frame.flags.writeable = False

                results = holistic.process(rgb_frame)

                landmarks = self._extract_keypoints(results)
                original_landmarks.append(landmarks)
                for augment_counter in range(num_augmentations):
                    processed_frame_landmarked = self.augment(rgb_frame, augment_counter, num_augmentations, operations,
                                                              noise_factor)
                    results = holistic.process(processed_frame_landmarked)
                    augmented_landmarks[augment_counter, frame_count, :] = self._extract_keypoints(results)

                rgb_frame.flags.writeable = True

                # Increment counter for frame extraction
                frame_count += 1

        cap.release()
        cv2.destroyAllWindows()

        # Repeat the last frame until the 30-frame requirement is satisfied for both original and augmented frames
        while len(original_landmarks) < num_frames:
            original_landmarks.append(original_landmarks[-1].copy())

        original_landmarks = np.array(original_landmarks)
        # Add the data for this video to class_data
        class_data = np.concatenate([class_data, original_landmarks[np.newaxis, ...], augmented_landmarks], axis=0)
        return class_data

    def _extract_keypoints(self, results):
        lh = np.array([[res.x, res.y, res.z] for res in
                        results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(
            21 * 3)
        rh = np.array([[res.x, res.y, res.z] for res in
                        results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(
            21 * 3)
        return np.concatenate([lh, rh])

    def save_class_data(self, class_name, class_data):
        numerical_label = self.class_mapping[class_name]
        encoder = OneHotEncoder(categories='auto', sparse=False)
        one_hot_label = encoder.fit_transform([[numerical_label]])
        class_output_dir = os.path.join(self.output_dir, class_name)
        os.makedirs(class_output_dir, exist_ok=True)
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
    data_preprocessor.preprocess_data(num_frames=30, num_augmentations=4)
    data_preprocessor.save_class_mapping(output_directory)
    data_preprocessor.shutdown()
