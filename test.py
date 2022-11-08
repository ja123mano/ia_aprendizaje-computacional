""" Archivo de prueba para cargar los descriptores de 1 imagen del archivo de images.obj """

import pickle
import os

with open(os.path.join(os.getcwd(), "images.obj"), "rb") as file:
    x = pickle.load(file)

print(x.get("Cultivo_124"))