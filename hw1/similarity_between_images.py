import cv2
import math
import numpy as np
from os import path

current = path.dirname(path.dirname(__file__))
img_path = path.join(current, "pictures")

"""
calculate difference between two signals 
1.NRMSE &&  2.PSNR
"""
def read_image(file_path):
    img = cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)
    img_2 = cv2.imread(file_path,cv2.IMREAD_COLOR)
    img = np.float32(img)
    img_2 = np.float32(img_2)
    return img , img_2

def NRMSE(pic_1,pic_2):
    sum_1 = 0
    sum_2 = 0
    for i in range(pic_1.shape[0]):
        for j in range(pic_1.shape[1]):
            sum_1 +=( (abs(pic_1[i][j]-pic_2[i][j]))**2 )
            sum_2 +=( (abs(pic_1[i][j]))**2 )
    return math.sqrt( (sum_1/sum_2) )
    
def PSNR(pic_1,pic_2):
    X_max = 255
    sum_1 = 0
    for color in range(3):
        for i in range(pic_1.shape[0]):
            for j in range(pic_1.shape[1]):
                sum_1 +=( (abs(pic_1[i][j][color] - pic_2[i][j][color]))**2 )
    """
    mse = np.mean( (pic_1-pic_2)**2 ) 
    """            
    result = 3 * pic_1.shape[0] * pic_1.shape[1] * (X_max**2) / sum_1
    return 10* math.log10(result)

def show(img,img_2,pic,pic_2):
    print("my PSNR: ",PSNR(img_2,pic_2))
    print("my NRMSE: ",NRMSE(img,pic))
    
    
img,img_2 = read_image(path.join(img_path,"1.bmp"))
pic,pic_2 = read_image(path.join(img_path,"2.bmp"))
print("opencv PSNR: ",cv2.PSNR(img_2,pic_2))
show(img,img_2,pic,pic_2)