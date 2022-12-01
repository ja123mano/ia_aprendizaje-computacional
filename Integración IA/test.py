import numpy as np
import pyautogui
import matplotlib.pyplot as plt
from skimage.transform import resize
from skimage.feature import graycomatrix, graycoprops
from skimage.color import rgb2gray
from skimage import img_as_ubyte

biomas_id = ["Agua", "Bosque", "Ciudad", "Cultivo", "Desierto", "Montaña"]

def start_reader():
    pass

def get_prediction(clf) -> str:
    scale = 15
    windows_task_bar = 40
    xbase, ybase = 0, 43
    w, h = pyautogui.size()
    width = w - xbase
    height = h - ybase - windows_task_bar

    rgb = np.array(pyautogui.screenshot(region=(xbase, ybase, width, height)))
    #plt.imshow(rgb)
    #plt.show()

    # Obtener el tamaño de la imagen a usar
    img_width = int(width/scale)
    img_height = int(height/scale)

    # Redimencionar la imagen y cambiarla a escala de grises
    rgb_resized = resize(rgb, (img_height, img_width), anti_aliasing=True)
    gray_resized = img_as_ubyte(rgb2gray(rgb_resized))

    # Obtener los descriptores de la imagen en escala de grises
    glcm = graycomatrix(gray_resized, distances=[5], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4])
    texture_desc = [graycoprops(glcm, 'dissimilarity')[0, 0], graycoprops(glcm, 'homogeneity')[0, 0], graycoprops(glcm, 'energy')[0, 0], graycoprops(glcm, 'correlation')[0, 0]]
    #print(texture_desc)
    # Hacer la predicción de la imagen tomada
    prediction = clf.predict([texture_desc])[0]
    return biomas_id[prediction]