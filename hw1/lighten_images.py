import cv2
import copy
import numpy as np
from os import path

current = path.dirname(path.dirname(__file__))
img_path = path.join(current, "pictures")
destination = path.join(path.dirname(__file__),"brighter_or_darker_results")

def image_handling(file_path,current_pic):
    
    # function that handle the brightness
    def handle(Y,op):
        return 255*( (Y/255)**op )
    
    img = cv2.imread(file_path)  # 3-D images BGR    
    print("The shape of image is: ",img.shape)
    
##########################################################
   
    """
        deal with grayscale picture
    """
    if np.array_equal(img[...,0],img[...,1]) and np.array_equal(img[...,1],img[...,2]):
        img = cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)
        brighten = copy.deepcopy(img)  # deep copy of img
        darken = copy.deepcopy(img)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                # op > 1 : darken
                darken[i][j] = handle(img[i][j],2)          # here choose op == 2
                # op < 1 : brighten
                brighten[i][j] = handle(img[i][j],0.5)        # here choose op == 0.5
        
        cv2.imwrite(destination+"\\"+str(current_pic)+"_brighten.bmp",brighten)
        cv2.imwrite(destination+"\\"+str(current_pic)+"_darken.bmp",darken) 
        cv2.imwrite(destination+"\\"+str(current_pic)+"_original.bmp",img)  
        return
    
###########################################################
    """
        If picture is RGB, three channels
    """
    img_original = copy.deepcopy(img)
    
    # turn BGR to Ycrcb coordinate
    img = cv2.cvtColor(img_original, cv2.COLOR_BGR2YCR_CB)
    brighten = copy.deepcopy(img)  # deep copy of img
    darken = copy.deepcopy(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # op > 1 : darken
            darken[i][j][0] = handle(img[i][j][0],2)          # here choose op == 2
            # op < 1 : brighten
            brighten[i][j][0] = handle(img[i][j][0],0.5)        # here choose op == 0.5
            
    # turn the coordinate back to the BGR
    img_brighten = cv2.cvtColor(brighten,cv2.COLOR_YCrCb2BGR)
    img_darken = cv2.cvtColor(darken,cv2.COLOR_YCrCb2BGR)
    # get brighter image:    
    cv2.imwrite(destination+"\\"+str(current_pic)+"_brighter.bmp",img_brighten)
    # get darker image:      
    cv2.imwrite(destination+"\\"+str(current_pic)+"_darker.bmp",img_darken) 
    cv2.imwrite(destination+"\\"+str(current_pic)+"_original.bmp",img_original)

# bmp files
for i in range(1,11):
    image_handling(img_path+"\\"+str(i)+".bmp" , i)