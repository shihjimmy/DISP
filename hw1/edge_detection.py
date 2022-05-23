import cv2 
import numpy as np
from os import path

### define kernel of edge detection
#1. Sobel operator for horizontal difference
#   you can get other direction's difference via rotating the kernel
kernel_sobel = np.array( ([1,0,-1],
                         [2,0,-2],
                         [1,0,-1]) ) 
kernel_sobel = np.divide(kernel_sobel,4)
#2. Laplacian operator 
kernel_laplacian = np.array( ([-1,-1,-1],
                             [-1, 8,-1],
                             [-1,-1,-1]) )
kernel_laplacian = np.divide(kernel_laplacian,8)

def edge_detection(file,mode,current_pic):
    
    def read_img_grayscale(file):
        # type of img will be a numpy.ndarray
        img = cv2.imread(file,cv2.IMREAD_GRAYSCALE)
        return img
    
    row = read_img_grayscale(file).shape[0]
    col = read_img_grayscale(file).shape[1]
    result_dir = path.join(path.dirname(__file__),'edge_detection_results')
    
    def horizontal_detection(img):
        new_img = np.zeros((row,col-1))
        for j in range(col-1):
            for i in range(row):
                new_img[i][j] = abs(img[i][j+1]-img[i][j])
        cv2.imwrite(result_dir+'\\'+str(current_pic)+'_result0.bmp',new_img)
        return
        
    def vertical_detection(img):
        new_img = np.zeros((row-1,col))
        for i in range(row-1):
            for j in range(col):
                new_img[i][j] = abs(img[i+1][j]-img[i][j])
        cv2.imwrite(result_dir+'\\'+str(current_pic)+'_result1.bmp',new_img)
        return
    
    def sobel_detection(img):
        new_img = np.zeros((row,col))
        for i in range(row-3):
            for j in range(col-3):
                val = 0
                for t in range(3):
                    for v in range(3):
                       val += img[i+t][j+v] * kernel_sobel[t][v]
                new_img[i][j] = abs(val) 
        cv2.imwrite(result_dir+'\\'+str(current_pic)+'_result2.bmp',new_img)
        return
    
    def laplacian_detection(img):
        new_img = np.zeros((row,col))
        for i in range(row-3):
            for j in range(col-3):
                val = 0
                for t in range(3):
                    for v in range(3):
                       val += img[i+t][j+v] * kernel_laplacian[t][v]
                new_img[i][j] = abs(val) 
        cv2.imwrite(result_dir+'\\'+str(current_pic)+'_result3.bmp',new_img)
        return
     
    img = read_img_grayscale(file)
    if   mode==0:
        horizontal_detection(img)
    elif mode==1:
        vertical_detection(img)
    elif mode==2:
        sobel_detection(img)
    else:
        laplacian_detection(img)

current = path.dirname(path.dirname(__file__))
img_path = path.join(current,'pictures')

#bmp files
for i in range(1,11):
    for mode in range(4):
        # mode 0: horizontal
        # mode 1: vertical
        # mode 2: sobel_detection
        # mode 3: laplacian_detection
        edge_detection(img_path+'\\'+str(i)+'.bmp',mode,i)
