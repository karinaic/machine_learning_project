from tensorflow.keras.layers import *
from tensorflow.keras.models import *
from tensorflow.keras.callbacks import *
from tensorflow.keras.optimizers import *

#pretrained network
from tensorflow.keras.applications.vgg16 import VGG16


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

    model.add(Conv2D(6, (5, 5), padding="same", input_shape=(30, 30, 3),activation='relu'))
    model.add(BatchNormalization())
    model.add(AveragePooling2D())

    model.add(Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
    model.add(BatchNormalization())

    model.add(MaxPooling2D(pool_size=(2, 2),  padding='same'))

    model.add(Flatten())

    model.add(Dense(units=120, activation='relu'))
    model.add(BatchNormalization())
    model.add(Flatten())
    model.add(Dropout(0.5))

    model.add(Dense(units=84, activation='relu'))
    model.add(BatchNormalization())
    model.add(Flatten())
    model.add(Dropout(0.5))
    model.add(Dense(43, activation = 'softmax',  kernel_regularizer= tf.keras.regularizers.l1_l2(l1=1e-4, l2=1e-3)))
    model.summary()

    return model


def pretrained_vgg16():
    base_model = VGG16(input_shape = (32, 32, 3), include_top=False,weights = 'imagenet')
    # Estableciendo a False las capas de la red VGG16 
    # no entreno las capas ya entrandas previamente en esa red  
    for layer in base_model.layers:
        layer.trainable = False
        ##### FULLY CONNECTED LAYER #####
        # Flatten the output layer to 1 dimension
    base_model.add(Flatten()(base_model.output))
    base_model.add(Dense(512, activation='relu'))
    base_model.add(Dropout(0.5))
    base_model.add(Dense(1, activation='sigmoid'))
    model = tf.keras.models.Model(base_model.input)
    model.summary()

def keras_particion(ruta_train, img_height, img_width, batch_size):
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(ruta_train, validation_split=0.25,subset="training",
    seed=43,image_size=(img_height, img_width),batch_size =batch_size)

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(ruta_train, validation_split=0.25, subset="validation",
    seed=43, image_size=(img_height, img_width),batch_size=batch_size)

    return train_ds, val_ds




    
