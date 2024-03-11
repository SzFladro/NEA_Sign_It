import os
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import multilabel_confusion_matrix, accuracy_score
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization, Dropout, Reshape, Bidirectional, LSTM, Flatten, Dense
from tensorflow.keras.callbacks import EarlyStopping, TensorBoard, ModelCheckpoint
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model, Sequential

# Load class mapping from the main directory
input_directory = os.path.join(os.getcwd(),'Neural network', 'Train_1')
class_mapping_path = os.path.join(input_directory, 'class_mapping.json')

with open(class_mapping_path, 'r') as f:
    class_mapping = json.load(f)

'''
    Loads pre-processed data as NumPy arrays for each class from a class_folder containing the extracted hand_landmarks and the appropriate class label
    One-Hot encodes labels to allow for easier training, distinction of categorical data 
    It splits the data and labels into the corresponding categories:
        Training: Used to fit and train the model to the set of data
        Validation: Used to evaluate the model after each epoch (training round) based on its performance with this set of data
        Testing: Used to finally evaluate the model after training has finished using new data that it hasn't seen
'''
def load_data(class_folder):
    labels = []
    landmarks_path = os.path.join(input_directory, class_folder, 'hand_landmarks.npy')
    landmarks = np.load(landmarks_path, allow_pickle = True)
    landmarks = np.concatenate([landmarks,landmarks],axis=0)
    labels.extend([class_mapping[class_folder]] * 180)    
    labels = to_categorical(labels, num_classes=len(class_mapping)).astype(int)
    X_train, X_test, y_train, y_test = train_test_split(landmarks, labels, test_size=0.3, random_state=42)
    X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=0.5, random_state=42)
    return X_train, X_test, X_val, y_train, y_test, y_val

#Creation of neural network structure and corresponding layers for a specific input_shape (size of NumPy arrays inputted containing data)
def Sequential_model(input_shape=(30, 1662)):
    model = Sequential()

    # LSTM Layers
    model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=input_shape))
    model.add(LSTM(128, return_sequences=True, activation='relu'))
    #return sequences is false, prevents the LTSM layer from returning sequences to the next Dnese layer
    model.add(LSTM(256, return_sequences=False, activation='relu'))

    model.add(Dropout(0.2))

    # Dense Layers 
    model.add(Dense(256, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(128, activation='relu'))

    model.add(BatchNormalization())
    # Output Layer
    model.add(Dense(len(class_mapping), activation='softmax'))

    return model

# Evaluates the final model with testing data and provides a final accuracy and a confusion matrix
def evaluate_model(X_test,y_test):
    model = tf.keras.models.load_model('BSLmodel.h5')
    model.load_weights('BSLweights.h5')
    model.summary()
    pred = model.predict(X_test)
    truelabel = np.argmax(y_test,axis=1).tolist()
    prediction = np.argmax(pred,axis=1).tolist()
    print(multilabel_confusion_matrix(truelabel, prediction))
    print(accuracy_score(truelabel, prediction))


'''
    Splits the training data into batches,
    Trains the neural network using a mini-batch gradient descent where the batch size is >1 but < size of training set,
    Uses Early stopping if the model stops improving
    TensorBoard provides a local dashboard of the models progress
    After each epoch, the model is evaluated based on validation data
    After training, the model is saved along with the weights
'''
def train_model(model, X_train, y_train, X_val, y_val, epochs=500, batch_size = 64):
    log_dir = os.path.join(os.getcwd(),'Neural network','Logger')

    tb_callback = TensorBoard(log_dir=log_dir)
    early_stopping = EarlyStopping(monitor='categorical_accuracy', patience = 30, restore_best_weights=True)
    history = model.fit(X_train, y_train, 
                        batch_size=batch_size,
                        epochs=epochs, 
                        shuffle=True, 
                        callbacks=[early_stopping,tb_callback], 
                        validation_data =(X_val, y_val))
    model.save('BSLmodel.h5')
    model.save_weights('BSLweights.h5')
    del model
    return history

# Compiles and starts the neural network training
def training(X_train,X_val, y_train, y_val):
    model = Sequential_model()
    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
    model.build((30,1662))
    model.summary()

    history = train_model(model, X_train, y_train, X_val, y_val)
    ## 103 is the number of times that the loss function is calculated and hyperparameters are updated with every epoch
    return history

if __name__ == "__main__":
    #Initialises NumPy arrays for the data (X) and labels (y)
    X_train = np.empty((0,30,1662))
    X_test = np.empty((0,30,1662))
    X_val = np.empty((0,30,1662))
    y_train = np.empty((0,26))
    y_test = np.empty((0,26))
    y_val = np.empty((0,26))
    # load data from every class (letters of the alphabet) and split them into training and testing data
    for class_name in class_mapping:
        data_train, data_test, data_val, label_train, label_test, label_val = load_data(class_name)
        X_train = np.concatenate([X_train,data_train],axis=0)
        X_test = np.concatenate([X_test,data_test],axis=0)
        X_val = np.concatenate([X_val,data_val],axis=0)
        y_train = np.concatenate([y_train,label_train],axis=0)
        y_test= np.concatenate([y_test,label_test],axis=0)
        y_val= np.concatenate([y_val,label_val],axis=0)

    history = training(X_train,X_val, y_train, y_val)
    evaluate_model(X_test,y_test)
