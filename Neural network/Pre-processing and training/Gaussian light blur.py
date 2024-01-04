import os
import cv2
import numpy as np

def process_video(input_video_path, output_video_path):
    cap = cv2.VideoCapture(input_video_path)

    total_resolution = 0
    total_frames = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Store the first frame as a reference
        if total_frames == 0:
            reference_frame = gray

        # Calculate absolute difference between the current frame and the reference frame
        frame_diff = cv2.absdiff(reference_frame, gray)

        # Apply thresholding to detect motion
        _, thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)

        # Find contours of the motion
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Assume the largest contour is the person
            largest_contour = max(contours, key=cv2.contourArea)

            # Create a bounding box around the detected person
            x, y, w, h = cv2.boundingRect(largest_contour)

            # Add a margin to include hands
            margin = 20
            x -= margin
            y -= margin
            w += 2 * margin
            h += 2 * margin

            # Ensure the bounding box is within the frame
            x = max(0, x)
            y = max(0, y)
            w = min(frame.shape[1] - x, w)
            h = min(frame.shape[0] - y, h)

            # Crop the frame while maintaining the original background
            cropped_frame = frame[y:y+h, x:x+w]

            # Calculate resolution and update averages
            resolution = cropped_frame.shape[1], cropped_frame.shape[0]  # (width, height)
            total_resolution += np.prod(resolution)
            total_frames += 1

            # Display the processed frame
            cv2.imshow('Processed Frame', cropped_frame)
        else:
            # No motion detected, use the original frame
            cropped_frame = frame

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Calculate average resolution
    average_resolution = (total_resolution // max(1, total_frames), ) * 2

    # Specify paths for the resized and blurred videos
    resized_output_path = output_video_path.replace(".mp4", "_resized.mp4")
    blurred_output_path = output_video_path.replace(".mp4", "_blurred.mp4")

    # Resize videos to the average resolution
    resize_videos(input_video_path, resized_output_path, average_resolution)

    # Apply Gaussian blur to the resized video
    apply_gaussian_blur(resized_output_path, blurred_output_path)


def resize_videos(input_video_path, output_video_path, target_resolution):
    cap = cv2.VideoCapture(input_video_path)

    # Set minimum width and height
    min_width, min_height = 500, 500

    # Ensure target resolution is above minimum values
    target_resolution = max(target_resolution[0], min_width), max(target_resolution[1], min_height)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 20.0, target_resolution, isColor=True)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame
        resized_frame = cv2.resize(frame, target_resolution)

        out.write(resized_frame)

        cv2.imshow('Resized Frame', resized_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


def apply_gaussian_blur(input_video_path, output_video_path):
    cap = cv2.VideoCapture(input_video_path)

    # Get video properties from the input video
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height), isColor=True)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Apply Gaussian blur to the frame
        blurred_frame = cv2.GaussianBlur(frame, (15, 15), 0)

        out.write(blurred_frame)

        cv2.imshow('Blurred Frame', blurred_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


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
                output_path = os.path.join(output_folder, filename)
                process_video(input_path, output_path)


def main():
    home_directory = os.path.expanduser("~")
    input_directory = os.path.join(home_directory, 'Videos', 'Dataset')
    output_directory = os.path.join(home_directory, 'Videos', 'Processed-Dataset')

    process_videos_in_directory(input_directory, output_directory)


if __name__ == "__main__":
    main()
