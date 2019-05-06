from scipy import ndimage
from scipy.ndimage.filters import convolve
from scipy import misc
import numpy as np
import cv2

img_input = cv2.imread("img.jpg", 0)

def gaussian_kernel(size, sigma):
    size = int(size) // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g
    
img_smoothed = convolve(img_input, gaussian_kernel(5, 1))

cv2.imshow('Output',img_smoothed)
cv2.waitKey(0)
cv2.destroyAllWindows()
