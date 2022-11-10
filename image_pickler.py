""" Archivo para serializar las imágenes o sus descriptores y guardarlos en un archivo con los datos serializados """
""" Para que funcione el código, ten las carpetas de cada bioma dentro de una carpeta llamada 'Images' """
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

main_path = os.getcwd()
images_path = os.path.join(main_path, "Images")
biomes_list = os.listdir(images_path)

def save_file(saving="Image", scale=15, gray=True, file_name="imageFile"):
    """
    Función para guardar los datos serializados de las imágenes o sus descriptores
    en un archivo serializado. El archivo resultante tendrá un diccionario de los
    datos seleccionados (imágenes o descriptores), donde la llave se define por el
    bioma y el número de la imagen.

    Parámetros
    ----------
    saving : str ['Image', 'Descriptor'] - default 'Image'
        Se refiere a si quieres serializar las imágenes o sus descriptores.
        Si elijes 'Descriptor' las imágenes usadas para los cálculos de descriptores serán en escala de grises

    scale : int - default 15
        El valor por el cual se dividirán las dimensiones de la imagen

    gray : bool - default True
        True si quieres usar imágenes en escala de grises, False si quieres a color

    file_name : str - default 'imageFile'
        El nombre del archivo final que tendrá los datos serializados.
        El archivo se guardará en la ruta del directorio de trabajo
    """

    img_width = int(1920/scale)
    img_height = int(1080/scale)
    
    new_dict = dict()

    for biome in biomes_list:
        biome_path = os.path.join(images_path, biome)
        images_list = os.listdir(biome_path)

        print(biome)
        for i, image in enumerate(images_list):
            print(f"{i+1}/{len(images_list)}")
            key = biome + "_" + str(i)
            final_image_path = os.path.join(biome_path, image)

            rgb = io.imread(final_image_path)
            rgb_resized = resize(rgb, (img_height, img_width), anti_aliasing=True)
            if gray or saving == "Descriptor":
                gray_resized = img_as_ubyte(rgb2gray(rgb_resized))

            if saving == "Image":
                if gray:
                    new_dict[key] = gray_resized
                else:
                    new_dict[key] = rgb_resized
            
            elif saving == "Descriptor":
                glcm = graycomatrix(gray_resized, distances=[5], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4])
                texture_desc = [graycoprops(glcm, 'dissimilarity')[0, 0], graycoprops(glcm, 'homogeneity')[0, 0], graycoprops(glcm, 'energy')[0, 0], graycoprops(glcm, 'correlation')[0, 0]]

                new_dict[key] = texture_desc

        print()

    with open(file_name + ".obj", "wb") as file:
        pickle.dump(new_dict, file)

def main():
    save_file(file_name="images_gray")

if __name__ == "__main__":
    main()