import os
import cv2
import mediapipe as mp


def process_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    #Goes through every frame within the video, converts frame to rgb and extracts landmarks from the hands 
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                draw_landmarks(frame, hand_landmarks)

        output_video.write(frame)

    cap.release()
    output_video.release()

    ##draws landmarks on the frame and connects the 'dots'
def draw_landmarks(frame, landmarks):
    h, w, _ = frame.shape

    for landmark in landmarks.landmark:
        x, y = int(landmark.x * w), int(landmark.y * h)
        cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)

    connections = [
        (0, 1), (1, 2), (2, 3), (3, 4),
        (0, 5), (5, 6), (6, 7), (7, 8),
        (0, 9), (9, 10), (10, 11), (11, 12),
        (0, 13), (13, 14), (14, 15), (15, 16),
        (0, 17), (17, 18), (18, 19), (19, 20)
    ]

    for connection in connections:
        cv2.line(frame, (int(landmarks.landmark[connection[0]].x * w),
                         int(landmarks.landmark[connection[0]].y * h)),
                 (int(landmarks.landmark[connection[1]].x * w),
                  int(landmarks.landmark[connection[1]].y * h)),
                 (0, 255, 0), 2)

    ##goes through each directory 
def process_videos_in_directory(input_directory, output_directory):
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Process videos in subdirectories A-Z
    for label in range(ord('A'), ord('Z') + 1):
        label_folder = chr(label)
        input_folder = os.path.join(input_directory, label_folder)

        if not os.path.exists(input_folder):
            continue

        output_folder = os.path.join(output_directory, label_folder)
        os.makedirs(output_folder, exist_ok=True)

        for filename in os.listdir(input_folder):
            if filename.endswith(".mp4"):
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, f"processed_{filename}")
                process_video(input_path, output_path)

def main():
    home_directory = os.path.expanduser("~")
    input_directory = os.path.join(home_directory, 'Videos', 'Flashback Express','Data')
    output_directory = os.path.join(home_directory, 'Videos', 'Copy')

    process_videos_in_directory(input_directory, output_directory)

if __name__ == "__main__":
    main()