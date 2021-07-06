# machine_learning_project
# MACHINE LEARNING MODEL FOR TRAFFIC SIGN DETECTION

##        CONVOLUTIONAL NEURAL NETWORKS

### Project Description
---

Traffic signs have been designed to be easily recognizable by the human brain, however for computer systems this classification continues to present its limitations in the recognition of their patterns.

This project consists of creating a predictive Machine Learning model for the automated recognition of traffic signs.

For our objective we are going to compare a traditional Super Vector Machine (SVM) classification model and a model based on convolutional neural networks (CNN), we will be changing its hyperparameters to solve its complexity and make the comparison of its results and the margin of error. that each one of them offers us.

For this study, we will use the data set compiled in real time during more than 10 hours of work by the Group Vision team of the German Traffic Sign Recognition Benchmark (GTSRB).

Finally we will stay with the best prediction result offered to us and we will create a traffic sign detector in images based on Deep Learning.

#### Dataset : 

+   Single-image, multi-class classification problem
+   More than 40 classes
+   More than 50,000 images in total
+   Large, lifelike database

#### Structure

+   The training set archive is structures as follows:
+   One directory per class
+   Each directory contains one CSV file with annotations ("GT-<ClassID>.csv") and the training images
+   Training images are grouped by tracks
+   Each track contains 30 images of one single physical traffic sign

#### Image format

+   The images contain one traffic sign each
+   Images contain a border of 10 % around the actual traffic sign (at least 5 pixels) to allow for edge-based approaches
+   Images are stored in PPM format (Portable Pixmap, P6)
+   Image sizes vary between 15x15 to 250x250 pixels
+   Images are not necessarily squared
+   The actual traffic sign is not necessarily centered within the image.This is true for images that were close to the image border in the full camera image
+   The bounding box of the traffic sign is part of the annotatinos (see below)


#### Keywords:
+   Artificial vision,
+   Deep Learning,
+   Object Detection,
+   Supervised Learning,
+   Neural Networks.
