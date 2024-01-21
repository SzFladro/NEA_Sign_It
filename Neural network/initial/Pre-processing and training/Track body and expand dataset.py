import os
import cv2
import mediapipe as mp
import platform

mp_holistic = mp.solutions.holistic  # Define mp_holistic globally
mp_drawing = mp.solutions.drawing_utils # Drawing utilities

def shutdown_system():
    os.system("shutdown /s /t 1")

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
    if results.left_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4), 
                                 mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                                 ) 
    # Draw right hand connections  
    if results.right_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4), 
                                 mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                 )

def process_video(input_path, output_path, holistic):
    cap = cv2.VideoCapture(input_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = holistic.process(rgb_frame)

        # Check for hand landmarks and draw connections
        draw_styled_landmarks(frame, results)

        output_video.write(frame)

    cap.release()
    output_video.release()

def process_videos_in_directory(input_directory, output_directory):
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    holistic = mp_holistic.Holistic()

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
                output_path = os.path.join(output_folder, f"tracked_{filename}")
                process_video(input_path, output_path, holistic)

    holistic.close()

def main():
    home_directory = os.path.expanduser("~")
    input_directory = os.path.join(home_directory, 'Videos', 'Edited-Dataset')
    output_directory = os.path.join(home_directory, 'Videos', 'Track')

    process_videos_in_directory(input_directory, output_directory)

if __name__ == "__main__":
    main()
    shutdown_system()
