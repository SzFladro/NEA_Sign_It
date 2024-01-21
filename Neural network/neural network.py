import os
import json
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization, Dropout, Reshape, Bidirectional, LSTM, Flatten, Dense
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam

# Load class mapping
home_directory = os.path.expanduser("~")
input_directory = os.path.join(home_directory, 'Videos', 'Train_2')
class_mapping_path = os.path.join(home_directory,'Videos','Train_2', 'class_mapping.json')

with open(class_mapping_path, 'r') as f:
    class_mapping = json.load(f)

# Function to load and preprocess data
def load_data(class_folder):
    landmarks_path = os.path.join(input_directory, class_folder, 'hand_landmarks.npy')
    labels_path = os.path.join(input_directory, class_folder, 'label.npy')

    landmarks = np.load(landmarks_path)
    labels = np.full((landmarks.shape[0],), class_mapping[class_folder])

    # Split data into 60-40 for training and testing
    X_train, X_test, y_train, y_test = train_test_split(landmarks, labels, test_size=0.05, random_state=42)
    print(X_train)

    return X_train, X_test, y_train, y_test

# Create the neural network model
class BSLRecognitionModel(tf.keras.Model):
    def __init__(self, input_shape=(30, 126), num_classes=26):
        super(BSLRecognitionModel, self).__init__()

        # LSTM Layers
        self.lstm1 = Bidirectional(LSTM(64, return_sequences=True, activation='relu'))
        self.lstm2 = Bidirectional(LSTM(128, return_sequences=True, activation='relu'))
        self.lstm3 = Bidirectional(LSTM(256, return_sequences=True, activation='relu'))

        # Flatten Layer
        self.flatten1 = Flatten()

        # Dense Layers with Dropout
        self.dense1 = Dense(256, activation='relu')
        self.dense2 = Dense(128, activation='relu')
        self.dense3 = Dense(64, activation='relu')
        self.batchnormal2 = BatchNormalization()

        # Output Layer
        self.output_layer = Dense(num_classes, activation='softmax')

    def call(self, inputs):
        x = self.lstm1(inputs)
        x = self.lstm2(x)
        x = self.lstm3(x)
        x = self.flatten1(x)
        x = self.dense1(x)
        x = self.dense2(x)
        x = self.dense3(x)
        x = self.batchnormal2(x)
        x = self.output_layer(x)
        return x

# Function to evaluate the model
def evaluate_model(model, X_test, y_test):
    y_pred = np.argmax(model.predict(X_test), axis=1)
    y_true = np.squeeze(y_test)

    # Confusion matrix
    confusion_mat = confusion_matrix(y_true, y_pred)
    print("Confusion Matrix:")
    print(confusion_mat)

    # Classification report
    class_report = classification_report(y_true, y_pred)
    print("Classification Report:")
    print(class_report)

# Compile the model
model = BSLRecognitionModel()
optimiser = Adam(learning_rate=0.001, clipvalue=0.5)  
model.compile(optimizer=optimiser, loss='categorical_crossentropy', metrics=['categorical_accuracy'])
model.build((None,30,126))

# Train the model for each class
for class_folder in os.listdir(input_directory):
    X_train, X_test, y_train, y_test = load_data(class_folder)

    # Convert labels to one-hot encoding
    y_train_one_hot = tf.keras.utils.to_categorical(y_train, num_classes=26)
    y_test_one_hot = tf.keras.utils.to_categorical(y_test, num_classes=26)

    # Train the model

    model.fit(X_train, y_train_one_hot, epochs=1000, validation_split=0.2, callbacks=[EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)])

    # Evaluate the model
    print(f"Evaluating model for class {class_folder}")
    evaluate_model(model, X_test, y_test)

# Save the trained model
model.save('bsl_recognition_model.h5')
