import numpy as np
import cv2 as cv
from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt

img = cv.imread('cv_test.png', 1)
cv2_imshow(img)

plt.imshow(img, cmap='gray', interpolation='bicubic')

#########

from google.colab import files
uploaded = files.upload()

#########

from skimage import data, io, filters
import cv2

image = io.imread("test.png")
io.imshow(image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
io.imshow(image)

edges = filters.sobel(image)
io.imshow(edges)
