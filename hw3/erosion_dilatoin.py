import cv2
import numpy as np
from os import path

current = path.dirname(__file__)
dest = path.join(current,"erosion_dilation")
img = cv2.imread(dest+"\\"+"test.bmp",cv2.IMREAD_GRAYSCALE)

def dilaiton_erosion_x3(img,mode):
    for time in range(3):
        for i in range(0,img.shape[0],2):
            for j in range(0,img.shape[1],2):
                if i-1>=0 and i+1<img.shape[0] and j-1>=0 and j+1<img.shape[1]:
                    if mode==1: # erosion
                        img[i][j] = min(img[i][j],img[i-1][j],img[i+1][j],img[i][j-1],img[i][j+1])
                    elif mode==0: # dilation
                        img[i][j] = max(img[i][j],img[i-1][j],img[i+1][j],img[i][j-1],img[i][j+1])
    return img
      
def closing(img):
    img = dilaiton_erosion_x3(img,0)
    img = dilaiton_erosion_x3(img,1)
    return img

def opening(img):
    img = dilaiton_erosion_x3(img,1)
    img = dilaiton_erosion_x3(img,0)
    return img
    
def image_saving(img):
    orig_img = img
    img = dilaiton_erosion_x3(img,1)
    #kernel = np.ones((3,3), np.uint8)
    #img = cv2.erode(img,kernel)
    cv2.imwrite(dest+"\\"+"erosion_result.bmp",img)
    img = orig_img
    img = dilaiton_erosion_x3(img,0)
    #kernel = np.ones((3,3), np.uint8)
    #img = cv2.dilate(img,kernel)
    cv2.imwrite(dest+"\\"+"dilation_result.bmp",img)
    img = orig_img
    img = closing(img)
    cv2.imwrite(dest+"\\"+"closing_result.bmp",img)
    img = orig_img
    img = opening(img)
    cv2.imwrite(dest+"\\"+"opening_result.bmp",img)

image_saving(img)            