# IA con aprendizaje computacional

Este proyecto se hizo para la clase de Sistemas Inteligentes en el **Tec de Monterrey Gdl** durante el semestre **ago-dic 2022**.

El equipo está conformado por:
  - José Miguel Pérez González - [Moringos7](https://github.com/Moringos7)
  - José Enrique Santana Martínez - [ja123mano](https://github.com/ja123mano)
  - Alejandro Castro Arévalo

## ¿De qué trata?

Este proyecto trabaja con machine learning, específicamente con clasificares lineales, de red neuronal y una red neuronal convolucional, además de métodos de agrupamiento. Todo esto se entreno con imágenes tomadas de diferentes biomas de México, obtenidas del software de [Google Earth](https://www.google.com/intl/es-419/earth/). El punto era que cada clasificador o red neuronal fuera capaz de identificar un bioma dada una imagen, mientras que los métodos de agrupamiento solamente agrupaban las diferentes características de una imagen, dado que sean similares.

## Parte I

La parte 1 constó del entrenamiento de los clasificadores y redes neuronales con 4 carácteristicas (desimilaridad, homogeneidad, energía y correlación) obtenidas de las imágenes y la obtención de distintas calificaciones por cada clasificador:
  - Exactitud
  - Recall
  - Precisión

Para la red convolucional se utilizaron las imágenes preescaladas a razón de 15:1 y en escala de grises. El proceso fue obtener diversas técnicas de obtención de características de estas imágenes preescaladas. Debido a la poca cantidad de épocas que se usaron para entrenar la red convolucional, sus calificaciones fueron bastante bajas.

Con los métodos de agrupamiento, se usaron las [4 características, serializadas en un archivo .obj](https://github.com/ja123mano/ia_aprendizaje-computacional/blob/main/images_descriptors.obj), de cada imagen y se agruparon conforme a similitudes de estas en gráficos de 3 ejes, dando como resultado grupos donde supuestamente se identificaban por bioma.

## Parte II

La parte 2 constó del uso del mejor modelo de clasificación para la realización de una aplicación que detectara el bioma en tiempo real, cuando se esté utilizando Google Earth. Esta parte se encuentra en la carpeta [Integración IA](https://github.com/ja123mano/ia_aprendizaje-computacional/tree/main/Integraci%C3%B3n%20IA) donde se puede encontrar un Readme que explica como usar la aplicación.


