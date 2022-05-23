import numpy as np
import cv2
from os import path

def construct_img():
    # Create a black image
    img = np.zeros((512,512))
    rx = 190
    ry = 250
    x0 = 256
    y0 = 256
    for i in range(512):
        for j in range(512):
            if (((i-x0)**2 / rx**2) + ((j-y0)**2 / ry**2)) <= 1:
                img[i][j] = 256
    return img

img = construct_img()
print(img)

dest = path.dirname(__file__)
cv2.imwrite(dest+"//"+"elliptic.jpg",img)

def calculate(img,num):
    res = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            res += abs(img[i][j])**num
    res = res**(1/num)
    return res

def Norm(img,mode):
    if mode == 0: #L0 norm
        num = 0
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img[i][j]!=0:
                    num+=1
        return num
    elif mode == 1: #L1 norm
        return calculate(img,1)
    elif mode == 2: #L2 norm
        return calculate(img,2)
    else: #L infinte norm
        max_num = -512
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if abs(img[i][j]) >= max_num:
                    max_num = abs(img[i][j])
        return max_num
    
def Moment(img,a,b):
    nx = 0
    ny = 0
    res1 = 0
    res2 = 0
    res3 = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            res1 += i*img[i][j]
            res2 += j*img[i][j]
            res3 += img[i][j]
    nx = res1/res3
    ny = res2/res3
    
    ans = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            ans += ( ((i-nx)**a) * ((j-ny)**b) * img[i][j] )
    return ans

for mode in range(0,4):
    print(Norm(img,mode))
    
print("Momoent m_2,0: ",Moment(img,2,0))
print("Momoent m_1,1: ",Moment(img,1,1))
print("Momoent m_0,2: ",Moment(img,0,2))