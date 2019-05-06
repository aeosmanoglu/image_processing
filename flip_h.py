import sys
import cv2
import numpy

img_input = cv2.imread("img.jpg", 1)
img_output=img_input.copy()

H = len(img_input)
W = len(img_input[0])

for h in range(H):
    for w in range(W):
        img_output[h][w][0] = img_input[H-1-h][w][0]
        img_output[h][w][1] = img_input[H-1-h][w][1]
        img_output[h][w][2] = img_input[H-1-h][w][2]
        
cv2.imshow('Output',img_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
