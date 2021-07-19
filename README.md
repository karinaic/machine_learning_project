# machine_learning_project
# MODELO DE APRENDIZAJE AUTOMÁTICO 

## RECONOCIMIENTO DE SEÑALES DE TRÁFICO UTILIZANDO 

## REDES NEURONALES CONVOLUCIONALES


![Image text](https://github.com/karinaic/machine_learning_project/blob/main/resources/german_trafic_.png)

### Descripción del Proyecto:

Las señales de tráfico han sido diseñadas para ser fácilmente reconocibles por el cerebro humano, sin embargo para los sistemas informáticos esta clasificación sigue presentando algunas limitaciones en el reconocimiento de sus patrones.

Este proyecto consiste en la creación de un modelo predictivo de Machine Learning para el reconocimiento automático de señales de tráfico.

Para nuestro objetivo vamos a comparar dos modelos de redes neuronales convolucionales (CNN),una de nuestra configuración y otra red pre-entrenada; cambiaremos sus hiperparámetros para resolver su complejidad y hacer la comparación de sus resultados y el margen. de error. que cada uno de ellos nos ofrece.

Para este estudio, utilizaremos el conjunto de datos recopilados en tiempo real durante más de 10 horas de trabajo por el equipo de Visión de Grupo del Benchmark de Reconocimiento de Señales de Tráfico de Alemania (GTSRB).

Finalmente nos quedaremos con el mejor resultado de predicción que se nos ofrezca y crearemos un detector de señales de tráfico en imágenes basado en Deep Learning.

#### Conjunto de datos : 

+ Problema de clasificación de una sola imagen y varias clases
+ Más de 40 clases
+ Más de 50.000 imágenes en total
+ Base de datos grande y realista

#### Estructura de los datos:

+ El conjunto de datos  de entrenamiento está estructurado de la siguiente manera:
+ Un directorio por clase
+ Cada directorio contiene un archivo CSV con anotaciones ("GT- <ClassID> .csv") y sus imágenes de entrenamiento
+ Las imágenes de entrenamiento están agrupadas por carpetas
+ Cada carpeta contiene 30 imágenes de una única señal de tráfico real.

#### Formato de Imágenes

+ Las imágenes contienen una señal de tráfico cada una.
+ Las imágenes contienen un borde del 10% alrededor de la señal de tráfico real (al menos 5 píxeles) para permitir enfoques basados ​​en bordes.
+ Las imágenes se almacenan en formato PPM (Portable Pixmap, P6)
+ Los tamaños de imagen varían entre 15x15 y 250x250 píxeles
+ Las imágenes no son necesariamente cuadradas.
+ La señal de tráfico real no está necesariamente centrada dentro de la imagen.

#### Palabras clave:
+   Visión artificial
+   Deep Learning,
+   Entrenamiento supervisado profundo
+   Redes Neuronales

### Breve Introducción

El Aprendizaje Profundo es un conjunto de algoritmos de Aprendizaje Automático que se 
centran en emular el enfoque de aprendizaje de los seres humanos, pudiendo modelar 
abstracciones de alto nivel de los datos utilizando arquitecturas computacionales que admiten 
operaciones no lineales. 

La arquitectura computacional más usada para el Deep Learning es la Red Neuronal. Estas redes 
neuronales están formadas por múltiples capas. Las neuronas de una capa están conectadas con 
las adyacentes por medio de conexiones, las cuales tienen asociado un peso.

### Red Neuronal Artificial

![imagen](https://github.com/karinaic/machine_learning_project/blob/main/resources/red_neuronal_artificial.png)

### La Red Neuronal Convolucional
La Red Neuronal Convolucional (Convolutional Neuronal Network, CNN o ConvNet) es una clase
de red de aprendizaje profundo, aplicada en el análisis visual de imágenes. Las principales 
aplicaciones que tiene son reconocimiento de imágenes y vídeos, clasificación de imágenes y 
procesamiento del lenguaje natural

![imagen](https://github.com/karinaic/machine_learning_project/blob/main/resources/cnn.jpg)

Este tipo de Red Neuronal, por medio de entrenamiento y aprendizaje supervisado, intenta 
imitar cómo funciona las neuronas en la corteza visual de nuestro cerebro. Por lo tanto, estas 
tienen muchas capas ocultas especializadas, las cuales siguen una jerarquía. Las primeras capas 
irán detectando líneas y curvas, las siguientes irán cada vez abstrayéndose más hasta poder 
identificar formas complejas. 

A continuación, vamos a mostrar las formas que sería capaz de reconocer cada capa de una CNN.
Realmente, son las formas que hace que una neurona de esa capa maximice su activación.

![imagen](https://github.com/karinaic/machine_learning_project/blob/main/resources/ejemplo_imagen.png)

#### CLASIFICACIÓN DE SEÑALES DE TRÁFICO 

Vamos a desarrollar y comparar algoritmos de clasificación de señales de tráfico. 
En primer lugar, mostraremos el conjunto de datos al que nos enfrentamos. A continuación, 
desarrollaremos los algoritmos utilizados y qué resultados han obtenido en el problema.

#### Conjunto de datos:

El conjunto de datos (dataset) que se va a usar para entrenar a los clasificadores es GTSRB (The 
German Traffic Sign Recognition Benchmark).
Está formado por 39 209 imágenes en el conjunto de entrenamiento y por 12 631 en el conjunto 
de pruebas (test). 
