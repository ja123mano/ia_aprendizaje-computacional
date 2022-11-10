""" Archivo de prueba para cargar las imágenes/descriptores e imprimir 1 a pantalla """

import pickle
import os

file = "images_gray.obj"
biomas = ["Agua", "Bosque", "Ciudad", "Cultivo", "Desierto", "Montaña"]
# Rango de num -> 0 a 334 
num = 124
imagen = biomas[3] + "_" + str(num)

with open(os.path.join(os.getcwd(), file), "rb") as file:
    x = pickle.load(file)
    y = x.get(imagen)

# Para elegir los descriptores de una imagen, cambia los parámetros de la variable imagen
print(f"El diccionario contiene {len(x)} valores")
print(imagen)
print(y)