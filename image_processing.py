#------------------------------------------------------------------------------------------------------------------
#   Image processing example
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

from skimage import io
from skimage.transform import resize
from skimage.feature import graycomatrix, graycoprops
from skimage.color import rgb2gray
from skimage import img_as_ubyte

#------------------------------------------------------------------------------------------------------------------
#   Load image
#------------------------------------------------------------------------------------------------------------------
scale = 1
img_width = int(1920/scale)
img_height = int(1080/scale)

rgb = io.imread('Imágenes/Ciudad/OMM_5.jpg')
rgb_resized = resize(rgb, (img_height, img_width), anti_aliasing=False)   

plt.imshow(rgb_resized)
plt.show()

#------------------------------------------------------------------------------------------------------------------
#   Color histograms
#------------------------------------------------------------------------------------------------------------------
nbins = 16

rh = np.histogram(rgb_resized[:,:,0].flatten(), nbins, density = True)
gh = np.histogram(rgb_resized[:,:,1].flatten(), nbins, density = True)
bh = np.histogram(rgb_resized[:,:,2].flatten(), nbins, density = True)

plt.plot(rh[0], 'r')
plt.plot(gh[0], 'g')
plt.plot(bh[0], 'b')
plt.xlabel('Bin')
plt.ylabel('Frequency')
plt.title('Color histograms')
#plt.show()

hist_descriptor = np.concatenate((rh[0], gh[0], bh[0]))

#------------------------------------------------------------------------------------------------------------------
#   Texture descriptors
#------------------------------------------------------------------------------------------------------------------

gray_resized = img_as_ubyte(rgb2gray(rgb_resized))
glcm = graycomatrix(gray_resized, distances=[5], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4])
    
texture_desc = [graycoprops(glcm, 'dissimilarity')[0, 0], graycoprops(glcm, 'homogeneity')[0, 0], 
             graycoprops(glcm, 'energy')[0, 0], graycoprops(glcm, 'correlation')[0, 0]]

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------