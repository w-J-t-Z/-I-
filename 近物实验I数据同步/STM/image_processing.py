import cv2
import numpy as np
from matplotlib import pyplot as plt

def localminima(imgP,SS):
    u=imgP[int((SS-1)/2),int((SS-1)/2)]
    for i in range(int(SS)):
        for j in range(int(SS)):
            if (imgP[i,j]<u):
                return False
    return True


# Read the original image
img = cv2.imread('database.png') 
# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_test=img_gray[150:256,10:256]
cv2.imshow('cut', img_test)
cv2.waitKey(0)

L=15
A=0.1
s0=2.5
kernel1=np.zeros((L,L),dtype='float32')
for i in range(L):
    for j in range(L):
        kernel1[i,j]=A*np.exp(-((i-(L-1)/2)**2+(j-(L-1)/2)**2)/(s0**2))
#kernel1=kernel1-np.average(kernel1)+1/(L*L)

img_k=cv2.filter2D(img_test,-1,kernel=kernel1)
cv2.imshow('k', img_k)
cv2.waitKey(0)
cv2.imwrite("imgK.png",img_k)


SS=23
img_select=np.ones((106,246),dtype='uint8')*255
for i in range(int((SS-1)/2),int(106-(SS-1)/2)):
    for j in range(int((SS-1)/2),int(246-(SS-1)/2)):
        if localminima(img_k[int(i-(SS-1)/2):int(i+(SS-1)/2+1),int(j-(SS-1)/2):int(j+(SS-1)/2+1)],SS):
            print(i,j)
            img_select[i,j]=0
cv2.imshow('select', img_select)
cv2.waitKey(0)
cv2.imwrite("imgSelect.png",img_select)