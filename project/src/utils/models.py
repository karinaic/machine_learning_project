from tensorflow.keras.layers import *
from tensorflow.keras.models import *
from tensorflow.keras.callbacks import *
from tensorflow.keras.optimizers import *

import tensorflow as tf
from tensorflow.keras.preprocessing import image
import json

def my_best_model():
    
    model = Sequential()
    model.add(Conv2D(filters = 64, kernel_size = (5,5), activation = 'relu', 
                    input_shape = (30, 30, 3), data_format = 'channels_last',
                    kernel_regularizer = tf.keras.regularizers.l1_l2(l1=1e-4, l2=1e-3)))
    model.add(BatchNormalization())
    model.add(Conv2D(filters = 64, kernel_size = (5,5), padding = "same", strides = (2, 2),
                    kernel_regularizer = tf.keras.regularizers.l1_l2(l1=1e-4, l2=1e-3)))
    model.add(BatchNormalization())
    model.add(Conv2D(filters = 128, kernel_size = (5,5), activation = 'relu' ,
                    kernel_regularizer=tf.keras.regularizers.l1_l2(l1=1e-4, l2=1e-3)))
    model.add(BatchNormalization())
    model.add(Dropout(0.3))
    model.add(Conv2D(filters = 128, kernel_size = (5,5), padding = "same",
                    kernel_regularizer = tf.keras.regularizers.l1_l2(l1=1e-4, l2=1e-3), strides = (2, 2)))
    model.add(BatchNormalization())
    model.add(Flatten())
    model.add(Dropout(0.3))
    model.add(Dense(1024, activation = 'relu',  kernel_regularizer= tf.keras.regularizers.l1_l2(l1=1e-4, l2=1e-3)))
    model.add(Dropout(0.4))
    model.add(Dense(256, activation = 'relu',  kernel_regularizer= tf.keras.regularizers.l1_l2(l1=1e-4, l2=1e-3)))
    model.add(Dropout(0.5))
    model.add(Dense(43, activation = 'softmax',  kernel_regularizer= tf.keras.regularizers.l1_l2(l1=1e-4, l2=1e-3)))
    model.summary()

    return model


def model_lenet_5():
    model = Sequential()
    model.add(Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(30, 30, 3))))
    model.add(AveragePooling2D())
    model.add(Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
    model.add(AveragePooling2D())
    model.add(Flatten())
    model.add(Dense(units=120, activation='relu'))
    model.add(Dense(units=84, activation='relu'))
    model.add(Dense(units=10, activation = 'softmax'))
    model.summary()

    return model


