""" Archivo para serializar los datos de las imágenes y guardarlos en un archivo llamado 'images.obj'"""
""" Para obtener los descriptores se usaron las imágenes redimencionadas a 128px x 72px y coloreadas en escalas de grises"""

import os
import pickle

import numpy as np
import matplotlib.pyplot as plt

from skimage import io
from skimage.transform import resize
from skimage.feature import graycomatrix, graycoprops
from skimage.color import rgb2gray
from skimage import img_as_ubyte

scale = 15
img_width = int(1920/scale)
img_height = int(1080/scale)

images_path = os.path.join(os.getcwd(), "Images")
biomes_list = os.listdir(images_path)
images_dict = dict()

for biome in biomes_list:
    biome_path = os.path.join(images_path, biome)
    images_list = os.listdir(biome_path)

    print(biome, "\n")

    for i, image in enumerate(images_list):
        print(f"{i+1}/{len(images_list)}")
        key = biome + "_" + str(i)
        final_image_path = os.path.join(biome_path, image)

        rgb = io.imread(final_image_path)
        rgb_resized = resize(rgb, (img_height, img_width), anti_aliasing=True)

        gray_resized = img_as_ubyte(rgb2gray(rgb_resized))
        glcm = graycomatrix(gray_resized, distances=[5], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4])
        texture_desc = [graycoprops(glcm, 'dissimilarity')[0, 0], graycoprops(glcm, 'homogeneity')[0, 0], graycoprops(glcm, 'energy')[0, 0], graycoprops(glcm, 'correlation')[0, 0]]

        images_dict[key] = texture_desc
    
    print("\n")

with open(os.path.join(os.getcwd(), "images.obj"), "wb") as file:
    pickle.dump(images_dict, file)