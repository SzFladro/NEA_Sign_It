import os
import cv2
import mediapipe as mp

'''
    Opens a video file and processes it, detecting and drawing landmarks for each frame within it
    Gets video properties and Processes each frame within the video, flipping it horizontally removing mirror look
    Detects landmarks and draws it on the frame, overwriting it

    Parameters:
        input_path (str): path to the input video file
        output_path (str): path for the edited video file with handlandmarks to be saved at
'''
def process_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    videofiletosave = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_path, videofiletosave, fps, (width, height))

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

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

'''
    Draws hand landmarks and connections on the given frames 
    
    Parameters:    
        frame (NumPy Array): input BGR openCV frame 
        landmarks: detected hand landmarks

'''
def draw_landmarks(frame, landmarks):
    h, w, _ = frame.shape

    #draws circles at each detected landmark
    for landmark in landmarks.landmark:
        x, y = int(landmark.x * w), int(landmark.y * h)
        cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)

    #Defines connections between landmarks
    connections = [
        (0, 1), (1, 2), (2, 3), (3, 4),
        (0, 5), (5, 6), (6, 7), (7, 8),
        (0, 9), (9, 10), (10, 11), (11, 12),
        (0, 13), (13, 14), (14, 15), (15, 16),
        (0, 17), (17, 18), (18, 19), (19, 20)
    ]

    #draws lines connecting connections
    for connection in connections:
        cv2.line(frame, (int(landmarks.landmark[connection[0]].x * w),
                         int(landmarks.landmark[connection[0]].y * h)),
                 (int(landmarks.landmark[connection[1]].x * w),
                  int(landmarks.landmark[connection[1]].y * h)),
                 (0, 255, 0), 2)

'''
    Processes all videos within the subdirectories A-Z in the input_directory
    Creates an output directory for the subdirectory of processes videos

    Parameters:
        input_directory (str): Directory containing subdirectories A-Z with video files
        output_directory (str): Directory to store processed videos
'''
def process_videos_in_directory(input_directory, output_directory):
    os.makedirs(output_directory, exist_ok=True)
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

#Main function to process videos in the specified directories
def main():
    home_directory = os.path.expanduser("~")
    input_directory = os.path.join(home_directory, 'Videos', 'Flashback Express','Data')
    output_directory = os.path.join(home_directory, 'Videos', 'Copy')

    process_videos_in_directory(input_directory, output_directory)

if __name__ == "__main__":
    main()