from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv3D, MaxPooling3D, Flatten, Dense, BatchNormalization

def build_3d_cnn(input_shape, num_classes):
    model = Sequential()

    # Convolutional Layer 1
    model.add(Conv3D(32, kernel_size=(3, 3, 3), activation='relu', input_shape=input_shape))
    model.add(MaxPooling3D(pool_size=(2, 2, 2)))
    model.add(BatchNormalization())

    # Convolutional Layer 2
    model.add(Conv3D(64, kernel_size=(3, 3, 3), activation='relu'))
    model.add(MaxPooling3D(pool_size=(2, 2, 2)))
    model.add(BatchNormalization())

    # Convolutional Layer 3
    model.add(Conv3D(128, kernel_size=(3, 3, 3), activation='relu'))
    model.add(MaxPooling3D(pool_size=(2, 2, 2)))
    model.add(BatchNormalization())

    # Convolutional Layer 4
    model.add(Conv3D(256, kernel_size=(3, 3, 3), activation='relu'))
    model.add(MaxPooling3D(pool_size=(2, 2, 2)))
    model.add(BatchNormalization())

    # Convolutional Layer 5
    model.add(Conv3D(512, kernel_size=(3, 3, 3), activation='relu'))
    model.add(MaxPooling3D(pool_size=(2, 2, 2)))
    model.add(BatchNormalization())

    # Convolutional Layer 6
    model.add(Conv3D(512, kernel_size=(3, 3, 3), activation='relu'))
    model.add(MaxPooling3D(pool_size=(2, 2, 2)))
    model.add(BatchNormalization())

    # Flatten Layer
    model.add(Flatten())

    # Dense Layers
    model.add(Dense(512, activation='relu'))
    model.add(BatchNormalization())

    model.add(Dense(256, activation='relu'))
    model.add(BatchNormalization())

    # Output Layer
    model.add(Dense(num_classes, activation='softmax'))

    return model

# Dimensions based on the data
input_shape = (300, 256, 256, 3)  # 30 frames, 256x256 resolution, 3 channels (RGB)

# Number of output classes (200 in your case)
num_classes = 200

# Build the 3D CNN model
model = build_3d_cnn(input_shape, num_classes)

# Display model summary
model.summary()
