import seaborn as sns
import matplotlib.pyplot as plt 
import tensorflow as tf
import pandas as pd
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

def diferentes_pixeles(train,test):
    trainDfDpiSubset = train[(train.Width < 80) & (train.Height < 80)];
    testDfDpiSubset = test[(test.Width < 80) & (test.Height < 80)];

    g = sns.JointGrid(x="Width", y="Height", data=trainDfDpiSubset)
    sns.kdeplot(trainDfDpiSubset.Width, trainDfDpiSubset.Height, cmap="Reds",
            shade=False, shade_lowest=False, ax=g.ax_joint)
    sns.kdeplot(testDfDpiSubset.Width, testDfDpiSubset.Height, cmap="Blues",
            shade=False, shade_lowest=False, ax=g.ax_joint)
    sns.distplot(trainDfDpiSubset.Width, kde=True, hist=False, color="r", ax=g.ax_marg_x, label='Train distribution')
    sns.distplot(testDfDpiSubset.Width, kde=True, hist=False, color="b", ax=g.ax_marg_x, label='Test distribution')
    sns.distplot(trainDfDpiSubset.Width, kde=True, hist=False, color="r", ax=g.ax_marg_y, vertical=True)
    sns.distplot(testDfDpiSubset.Height, kde=True, hist=False, color="b", ax=g.ax_marg_y, vertical=True)
    g.fig.set_figwidth(10)
    g.fig.set_figheight(6)
    plt.show();
    plt.savefig('../resources/diferentes_pixeles.png')

def spent_time():
    time = pd.DataFrame({'Time': [0.10, 0.60 , 0.30 ],'Task': ['Buscar base de datos', 'Entrenamiento model-clasi', 'Flask/Streamlit']})
    plot = time.plot.pie(y='Time', autopct='%1.2f%%',shadow=True, figsize=(5, 5))
    labels = 'Buscar base de datos', 'Entrenamiento de model-clasi','Flask/Streamlit'
    plt.legend(labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    plt.show()
    return plot