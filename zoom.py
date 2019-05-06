import cv2
import numpy as np
import math

img_input = cv2.imread("img.jpg", 1)
rows = len(img_input[0])
cols = len (img_input)

zooming_factor = 4

new_rows = rows * zooming_factor
new_cols = cols * zooming_factor

img = np.zeros([new_cols,new_rows,3],dtype=np.uint8)
img.fill(255)

for x in range(rows):
    for y in range(cols):
        for z in range(zooming_factor):
            for w in range(zooming_factor):
                img[y * zooming_factor+z][x*zooming_factor+w] =img_input[y][x]

cv2.imshow('Output',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
