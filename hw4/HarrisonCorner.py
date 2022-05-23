import cv2
import numpy as np
from os import path
from scipy import signal
from scipy import fft

current = path.dirname(__file__)
dest = path.join(current,"HarrisonCorner_results")

def CornerDetection(file_path,window_size,num):
    input_img = cv2.imread(file_path)
    output_img = input_img.copy()
    
    offset = int(window_size/2)
    y_range = input_img.shape[0] - offset
    x_range = input_img.shape[1] - offset
    
    """
     X= conv2(I, [-1, 0, 1], 'same')
     Y= conv2(I, [-1, 0, 1]', 'same')
     
     A 是由 X.^2 和 w 做 convolution 而得出
     B 是由 Y.^2 和 w 做 convolution 而得出
     C 是由 X.*Y 和 w 做 convolution 而得出
     
     R = det(M) - k*Tr(M)^2
       = AB - C.^2 - k*(A+B).^2
       k 建議設為0.04 (根據經驗)

     corner 的選取要滿足以下的條件
     (i)  R[m, n] >= R[m+m1, n+n1],  -1 <= m1, n1 <=n1
     (ii) R[m, n] >=  threshold
          threshold 可以選為 Max(R)/100
    """

    dy,dx,dz= np.gradient(input_img)
    Ixx = dx**2
    Ixy = dy*dx
    Iyy = dy**2
    
    for y in range(offset, y_range):
        for x in range(offset, x_range):
            
            #Values of sliding window
            start_y = y - offset
            end_y = y + offset + 1
            start_x = x - offset
            end_x = x + offset + 1
            
            #The variable names are representative to 
            #the variable of the Harris corner equation
            windowIxx = Ixx[start_y : end_y, start_x : end_x]
            windowIxy = Ixy[start_y : end_y, start_x : end_x]
            windowIyy = Iyy[start_y : end_y, start_x : end_x]
            
            #Sum of squares of intensities of partial derevatives 
            Sxx = windowIxx.sum()
            Sxy = windowIxy.sum()
            Syy = windowIyy.sum()

            #Calculate determinant and trace of the matrix
            det = (Sxx * Syy) - (Sxy**2)
            trace = Sxx + Syy
            
            #Calculate r for Harris Corner equation
            k = 0.04
            r = det - k*(trace**2)
            threshold = np.max(r)/100

            if r > threshold:
                output_img[y,x] = (0,0,255)
    
    cv2.imwrite(dest+"\\"+"ex"+str(num)+"_result.png",output_img)
    return
    
for i in range(1,7):
    file_path = dest+"\\"+"ex"+str(i)+".png"
    CornerDetection(file_path,5,i)