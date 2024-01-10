import os
import numpy as np

home_directory = os.path.expanduser("~")
output_directory = os.path.join(home_directory, 'Videos', 'Train_2')

# Assuming you want to load the hand_landmarks.npy from a specific class folder, change 'class_name' accordingly
class_name = 'B'
file_path = os.path.join(output_directory, class_name, 'hand_landmarks.npy')

# Load the data
loaded_data = np.load(file_path, allow_pickle=True)

# Display the shape
print(f"Shape of hand_landmarks.npy in {class_name}: {loaded_data.shape}")
print(loaded_data)

