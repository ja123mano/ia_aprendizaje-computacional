import numpy as np
import pickle
import pyautogui
import matplotlib.pyplot as plt
from skimage.transform import resize
from skimage.feature import graycomatrix, graycoprops
from skimage.color import rgb2gray
from skimage import img_as_ubyte

with open(r"D:\(Documentos Escritorio)\Universidad\9° Semestre\Sistemas Inteligentes\Scripts\3p\Integración IA\MLPClassifier.clf", "rb") as file:
    clf = pickle.load(file)

biomas_id = ["Agua", "Bosque", "Ciudad", "Cultivo", "Desierto", "Montaña"]
scale = 15
xbase, ybase, w, h = 0, 43, 1920, 1035
width = w - xbase
height = h - ybase

rgb = np.array(pyautogui.screenshot(region=(xbase, ybase, w, h)))
plt.imshow(rgb)
plt.show()

img_width = int(width/scale)
img_height = int(height/scale)

rgb_resized = resize(rgb, (img_height, img_width), anti_aliasing=True)
gray_resized = img_as_ubyte(rgb2gray(rgb_resized))

glcm = graycomatrix(gray_resized, distances=[5], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4])
texture_desc = [graycoprops(glcm, 'dissimilarity')[0, 0], graycoprops(glcm, 'homogeneity')[0, 0], graycoprops(glcm, 'energy')[0, 0], graycoprops(glcm, 'correlation')[0, 0]]

print(texture_desc)

prediction = clf.predict([texture_desc])[0]
print(f"El bioma predicho es {biomas_id[prediction]}")