import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('img.jpg')
image=img.copy()
img = cv2.fastNlMeansDenoisingColored(img,None,5,3,7,15)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cv2.imshow('image', img)
cv2.imshow('image2', thresh)
print(img.dtype)
print(thresh.dtype)
# noise removal
kernel = np.ones((3,3),np.uint8)
img = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel, iterations = 2)
img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
print(img[1,4])
edges = np.uint8(cv2.Canny(img,100,200))
edges=cv2.cvtColor(edges,cv2.COLOR_GRAY2RGB)
print(edges[1,4])
edgeinv = cv2.bitwise_not(edges)
cv2.namedWindow('edgeinv',cv2.WINDOW_NORMAL)
cv2.resizeWindow('edgeinv', 1000,1000)
cv2.imshow('edgeinv',edgeinv)
for i in range(1561):
    for j in range(1999):
        if (edgeinv[i,j]==[0,0,0]).all():
            edgeinv[i,j]= [0,255,0]
cv2.imshow('after', img)
cv2.imshow('edges', edges)
cv2.imshow('edgeinv', edgeinv)
cv2.imshow('clone',image)
print(image.shape)
print(edges.shape)
output = cv2.bitwise_and(image,edgeinv,mask=None)
cv2.namedWindow('output',cv2.WINDOW_NORMAL)
cv2.resizeWindow('output', 1000,1000)
cv2.imshow('output',output)
cv2.waitKey(0)
cv2.destroyAllWindows()

