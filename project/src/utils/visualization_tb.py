import seaborn as sns
import matplotlib.pyplot as plt 
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow import keras
import os, sys


def frequency_class(df):
    c = df['ClassId'].nunique()
    x = df['ClassId'].value_counts()
    plt.bar(x=x.index.sort_values(), height=x, color='hotpink')
    plt.title('Numbers of sample in each class', color='black')
    plt.xlabel("Class ID", color='black')
    plt.ylabel("Samples", color='black')
    plt.tick_params(colors='black')
    plt.savefig('../resources/number_samples_class.png') 

def labels_images(x):
    plt.figure(figsize=(10, 15))
    for images, labels in x.take(1):
        for i in range(9):
            ax = plt.subplot(3, 3, i + 1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(int(labels[i]))
            plt.axis("off")
            plt.savefig('../resources/labels_images.png')

def images_shape(x):
    for image_batch, labels_batch in x:
        print("Images shape for batch:",image_batch.shape)
        print("Shape of label for batch:", labels_batch.shape)
        print("First label batch:",labels_batch[0])
        break


def plot_accuracy(x):
    plt.figure(0)
    plt.plot(x.x['accuracy'], label= 'train accuracy')
    plt.plot(x.x['val_accuracy'], label= 'val accuracy')
    plt.title('Accuracy')
    plt.xlabel('epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.savefig('../resources/plot_accuracy.png')


def plot_loss(x):
    plt.figure(0)
    plt.plot(x.x['loss'], label= 'train loss')
    plt.plot(x.x['val_loss'], label= 'val loss')
    plt.title('Loss')
    plt.xlabel('epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig('../resources/plot_loss.png')

def distribucion_clases(train,test):
    fig, axs = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(25, 6))
    axs[0].set_title('Train classes distribution')
    axs[0].set_xlabel('Class')
    axs[0].set_ylabel('Count')
    axs[1].set_title('Test classes distribution')
    axs[1].set_xlabel('Class')
    axs[1].set_ylabel('Count')

    sns.countplot(train.ClassId, ax=axs[0])
    sns.countplot(test.ClassId, ax=axs[1])
    axs[0].set_xlabel('Class ID');
    axs[1].set_xlabel('Class ID');
    plt.savefig('../resources/imagen_size_distribucion.png')

