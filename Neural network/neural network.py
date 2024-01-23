import os
import json
import numpy as np
import tensorflow as tf
import visualkeras
from PIL import ImageFont
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization, Dropout, Reshape, Bidirectional, LSTM, Flatten, Dense
from tensorflow.keras.callbacks import EarlyStopping, TensorBoard
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model, Sequential

# Load class mapping
input_directory = os.path.join(os.getcwd(),'Neural network', 'Train_1')
class_mapping_path = os.path.join(input_directory, 'class_mapping.json')

with open(class_mapping_path, 'r') as f:
    class_mapping = json.load(f)

# Function to load and preprocess data
def load_data(labels,class_folder):
    landmarks_path = os.path.join(input_directory, class_folder, 'hand_landmarks.npy')
    landmarks = np.load(landmarks_path, allow_pickle = True)
    landmarks = np.concatenate([landmarks,landmarks],axis=0)
    labels.extend([class_mapping[class_folder]] * 180)    
    return labels, landmarks

def Sequential_model(input_shape=(30, 1662)):
    model = Sequential()

    # LSTM Layers
    model.add(LSTM(26, return_sequences=True, activation='relu', input_shape=input_shape))
    model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=input_shape))
    model.add(LSTM(128, return_sequences=True, activation='relu'))
    model.add(LSTM(256, return_sequences=False, activation='relu'))

    # Flatten Layer
    model.add(Flatten())

    # Dense Layers with Dropout
    model.add(Dense(128, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(BatchNormalization())

    # Output Layer
    model.add(Dense(len(class_mapping), activation='softmax'))

    return model

def visualise(model):
    font = ImageFont.truetype("arial.ttf",12)
    visualkeras.layered_view(model, legend = True, font = font, spacing = 100)

def train_model(model, X_train, y_train,epochs=2000):
    early_stopping = EarlyStopping(monitor='categorical_accuracy', patience=5, restore_best_weights=True)
    log_dir = os.path.join(os.getcwd(),'Neural network','Logs')
    tb_callback = TensorBoard(log_dir=log_dir)

    model.fit(X_train, y_train, epochs=epochs, shuffle=True, callbacks=[early_stopping, tb_callback])
    model.save('BSLmodel.h5')
    model.save_weights('BSLweights.h5')
    del model

if __name__ == "__main__":
    labels = []
    Data = np.empty((0,30,1662))

    # Compile the model
    model = Sequential_model()
    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

    # load data from every class (letters of the alphabet) and split them into training and testing data
    for class_name in class_mapping:
        labels , landmarks = load_data(labels,class_name)
        Data = np.concatenate([Data , landmarks],axis=0)

    labels = to_categorical(labels, num_classes=len(class_mapping)).astype(int)
    print(labels)
    X_train, X_test, y_train, y_test = train_test_split(Data, labels, test_size=0.3, random_state=42)

    print(f"Number of unique classes: {len(np.unique(np.argmax(labels, axis=1)))}")
    
    # Train the model
    train_model(model, X_train, y_train)