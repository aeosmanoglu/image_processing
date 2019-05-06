import sys
import cv2
import numpy
img_input = cv2.imread("img.jpg", 1)

img_output=img_input.copy()
for i in range(len(img_input)):
    for j in range(len(img_input[0])):

        img_output[i][j][0] = 255 - img_input[i][j][0]
        img_output[i][j][1] = 255 - img_input[i][j][1]
        img_output[i][j][2] = 255 - img_input[i][j][2]

cv2.imshow('Output',img_output)

cv2.waitKey(0)
cv2.destroyAllWindows()
