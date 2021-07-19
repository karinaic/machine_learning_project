import os
import sys
import requests
from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.keras import preprocessing

dir = os.path.dirname
sep = os.sep
project_path = dir(dir(dir(os.path.abspath(__file__))))
sys.path.append(project_path)

from src.utils import models as mo
from src.utils import folders_tb as fo

menu = st.sidebar.selectbox('Menu:', options=["Bienvenida", "Visualizacion","Flask Api", "Modelos de Prediccion","Técnicas utilizadas","SQL Database"])

if menu == 'Bienvenida':
    st.title('CLASIFICADOR DE SEÑALES DE TRÁFICO')
    st.header("PROYECTO DE MACHINE LEARNING")
    st.write("Para este estudio, utilizaremos el conjunto de datos recopilados en tiempo real durante más de 10 horas de trabajo por el equipo de Visión de Grupo del Benchmark de Reconocimiento de Señales de Tráfico de Alemania (GTSRB)")
    project_path = dir(dir(dir(os.path.abspath(__file__))))
    image_1 = Image.open(project_path + sep + 'resources' + sep + 'cnn.jpg')
    st.image(image_1, use_column_width=True)

if menu == 'Técnicas utilizadas':
    st.title('Redes Neuronales Convolucionales')
    st.write('Las CNN sone una clase de red de aprendizaje profundo, aplicada en el análisis visual de imágenes.')
    st.write("Este tipo de Red Neuronal, por medio de entrenamiento y aprendizaje supervisado, intenta imitar cómo funciona las neuronas en la corteza visual de nuestro cerebro.")
    project_path = dir(dir(dir(os.path.abspath(__file__))))
    image_2 = Image.open(project_path + sep + 'resources' + sep + 'red_neuronal_artificial.png')
    st.image(image_2, use_column_width=True)

if menu == 'Flask_API':
    url= "http://localhost:6060/"
    json_api = requests.get(url).json()
    st.write(json_api)