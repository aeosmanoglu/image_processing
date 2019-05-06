import cv2
import numpy
import math

img_input = cv2.imread("img.jpg", 1)
rotate = 180
centerX = (len(img_input) // 2)
centerY = (len(img_input[0]) // 2)

def rotate_x (d,x,y):
    return int((math.cos(math.radians(d))*(x-centerX))-(math.sin(math.radians(d))*(y-centerY))+centerX)
    
def rotate_y (d,x,y):
    return int((math.sin(math.radians(d))*(x-centerX))-(math.cos(math.radians(d))*(y-centerY))+centerY)
    
img_output=img_input.copy()
img_output.fill(255)

for x in range(len(img_input)):
    for y in range(len(img_input[0])):
        new_x = rotate_x(rotate, x, y) -1
        new_y = rotate_y(rotate, x, y) -1
        img_output[new_x][new_y][0] = img_input[x][y][0] % 255
        img_output[new_x][new_y][1] = img_input[x][y][1] % 255
        img_output[new_x][new_y][2] = img_input[x][y][2] % 255
        
cv2.imshow('Output',img_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
