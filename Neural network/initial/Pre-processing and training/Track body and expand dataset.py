import os
import cv2
import mediapipe as mp
import platform

mp_holistic = mp.solutions.holistic  # Define mp_holistic globally
mp_drawing = mp.solutions.drawing_utils # Drawing utilities

#Shuts down the computer when the code has finished executing
def shutdown_system():
    os.system("shutdown /s /t 1")

'''
    Draws landmarks on input image based on Holistic results

    Parameters:
        image (NumPy array): input frame from the webcam
        results (tuple): Extracted coordinates of the different landmakrs from an image ran through a mediapipe model
'''
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

'''
    Processes video files, extracts landmakrs and saves the output to a new video file within the output_path
    Utilising the fourcc coded for decompression of the video file
'''
def process_video(input_path, output_path, holistic):
    cap = cv2.VideoCapture(input_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    codecused = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_path, codecused, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = holistic.process(rgb_frame)

        # Checks for hand landmarks and draws connections
        draw_styled_landmarks(frame, results)

        output_video.write(frame)

    cap.release()
    output_video.release()

'''
    Processes all videos within the subdirectories A-Z in the input_directory
    Creates an output directory for the subdirectory of processes videos

    Parameters:
        input_directory (str): Directory containing subdirectories A-Z with video files
        output_directory (str): Directory to store processed videos
'''
def process_videos_in_directory(input_directory, output_directory):
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

# Main function which processes videos within a specific directory, shutting down the computer afterwards
def main():
    home_directory = os.path.expanduser("~")
    input_directory = os.path.join(home_directory, 'Videos', 'Edited-Dataset')
    output_directory = os.path.join(home_directory, 'Videos', 'Track')
    process_videos_in_directory(input_directory, output_directory)

if __name__ == "__main__":
    main()
    shutdown_system()
