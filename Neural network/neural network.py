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
def load_data(class_folder):
    labels = []
    landmarks_path = os.path.join(input_directory, class_folder, 'hand_landmarks.npy')
    landmarks = np.load(landmarks_path, allow_pickle = True)
    landmarks = np.concatenate([landmarks,landmarks],axis=0)
    labels.extend([class_mapping[class_folder]] * 180)    
    labels = to_categorical(labels, num_classes=len(class_mapping)).astype(int)
    X_train, X_test, y_train, y_test = train_test_split(landmarks, labels, test_size=0.4, random_state=42)
    X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=0.5, random_state=42)
    return X_train, X_test, X_val, y_train, y_test, y_val

def Sequential_model(input_shape=(30, 1662)):
    model = Sequential()

    # LSTM Layers
    model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=input_shape))
    model.add(LSTM(128, return_sequences=True, activation='relu'))
    ##return sequences is false, prevents the LTSM layer from returning sequences to the next Dense layer
    model.add(LSTM(256, return_sequences=False, activation='relu'))

    model.add(BatchNormalization())

    # Dense Layers with Dropout
    model.add(Dense(256, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dense(128, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dense(64, activation='relu'))
    model.add(BatchNormalization())

    # Output Layer
    model.add(Dense(len(class_mapping), activation='softmax'))

    return model

def visualise(model):
    font = ImageFont.truetype("arial.ttf",12)
    visualkeras.layered_view(model, legend = True, font = font, spacing = 100)

    ##using mini-batch gradient descent to train the neural network (using a batch size that is >1 but < training set)
def train_model(model, X_train, y_train, X_val, y_val, epochs=1000, batch_size = 64):
    log_dir = os.path.join(os.getcwd(),'Neural network','Logger')
    tb_callback = TensorBoard(log_dir=log_dir)

    history = model.fit(X_train, y_train, 
                        batch_size=batch_size,
                        epochs=epochs, 
                        shuffle=True, 
                        callbacks=[tb_callback], 
                        validation_data =(X_val, y_val))
    model.save('BSLmodel.h5')
    model.save_weights('BSLweights.h5')
    del model
    return history

if __name__ == "__main__":
    X_train = np.empty((0,30,1662))
    X_test = np.empty((0,30,1662))
    X_val = np.empty((0,30,1662))
    y_train = np.empty((0,26))
    y_test = np.empty((0,26))
    y_val = np.empty((0,26))

    # Compile the model
    model = Sequential_model()
    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
    # load data from every class (letters of the alphabet) and split them into training and testing data
    for class_name in class_mapping:
        data_train, data_test, data_val, label_train, label_test, label_val = load_data(class_name)
        X_train = np.concatenate([X_train,data_train],axis=0)
        X_test = np.concatenate([X_test,data_test],axis=0)
        X_val = np.concatenate([X_val,data_val],axis=0)
        y_train = np.concatenate([y_train,label_train],axis=0)
        y_test= np.concatenate([y_test,label_test],axis=0)
        y_val= np.concatenate([y_val,label_val],axis=0)


    # Train the model
    history = train_model(model, X_train, y_train, X_val, y_val)
    ## 103 is the number of times that the loss function is calculated and hyperparameters are updated with every epoch