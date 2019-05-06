import cv2
import numpy as np
import math

img_input = cv2.imread("img.jpg", 1)
rows = len(img_input[0])
cols = len (img_input)

zooming_factor = 0.5
factor = int (1 / zooming_factor)
new_rows = int(rows * zooming_factor)
new_cols = int(cols * zooming_factor)

img = np.zeros([new_cols,new_rows,3],dtype=np.uint8)
img.fill(255)

for x in range(new_rows):
    for y in range(new_cols):
        c = np.zeros([3],int)
        for z in range(factor):
            for w in range(factor):
                c[0] += img_input[y * factor+z][x*factor+w][0]
                c[1] += img_input[y * factor + z][x * factor + w][1]
                c[2] += img_input[y * factor + z][x * factor + w][2]
        img[y][x][0] = c[0]//(factor*factor)
        img[y][x][1] = c[1]//(factor*factor)
        img[y][x][2] = c[2]//(factor*factor)
        
cv2.imshow('Output',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
