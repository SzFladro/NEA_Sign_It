import tensorflow as tf
from tensorflow.keras.layers import Conv3D, MaxPooling3D, Flatten, Dense, Dropout, LSTM, Reshape, BatchNormalization, Bidirectional
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.optimizers import Adam

additional_metrics = ['categoricalaccuracy']
loss_function = CategoricalCrossentropy()
number_of_epochs = 200
patience = 5
optimiser = Adam()
validation_split = 0.20
verbosity_mode = 1

#creation of a custom neural network 
class BSLRecognitionModel(tf.keras.Model):
    def __init__(self, input_shape=(20, 500, 500, 3), num_classes=26):
        super(BSLRecognitionModel, self).__init__()

        self.conv1 = Conv3D(64, kernel_size=(3, 3, 3),activation ='relu')
        self.pool1 = MaxPooling3D()
        self.conv2 = Conv3D(128, kernel_size=(3, 3, 3), activation = 'softmax')
        self.pool2 = MaxPooling3D()
        self.conv3 = Conv3D(64, kernel_size=(3, 3, 3), activation = 'softmax')
        self.pool3 = MaxPooling3D()
        self.batchnormal1 = BatchNormalization()  
        self.drop1 = Dropout(0.25)

        # Reshape layer
        self.reshape = Reshape((2, 60 * 60 * 64))

        # LSTM Layers
        self.lstm1 = Bidirectional(LSTM(64, return_sequences=True,activation='tanh'))
        self.lstm2 = Bidirectional(LSTM(128, return_sequences=True,activation='tanh'))
        self.lstm3 = Bidirectional(LSTM(256, return_sequences=True,activation='tanh'))

        # Flatten Layer
        self.flatten1 = Flatten()

        # Dense Layers with Dropout
        self.dense1 = Dense(256, activation='relu')
        self.dense2 = Dense(128, activation='relu')
        self.batchnormal2 = BatchNormalization()    

        # Output Layer
        self.output_layer = Dense(num_classes, activation='softmax')

    def call(self, inputs):
        x = self.conv1(inputs)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.pool2(x)
        x = self.conv3(x)
        x = self.pool3(x)
        x= self.batchnormal1(x)
        x = self.drop1(x)
        x = self.reshape(x)
        x = self.lstm1(x)
        x = self.lstm2(x)
        x = self.lstm3(x)
        x = self.flatten1(x)
        x = self.dense1(x)
        x = self.dense2(x)
        x = self.batchnormal2(x)
        x = self.output_layer(x)
        return x

# Create an instance of the model
model = BSLRecognitionModel()

# Display model summary
model.build((None, 20, 500, 500, 3))
model.compile(optimizer=optimiser, loss='categorical_crossentropy', metrics=additional_metrics)
early_stopping = EarlyStopping(monitor='categoricalaccuracy' ,patience = patience, restore_best_weights=True)
model.summary()
