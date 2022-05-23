import cv2
import numpy as np
from scipy import fft
from os import path

current = path.dirname(__file__)
dest = path.join(current,"fft_results")

img_high = cv2.imread(dest+"\\"+"1.jpg",cv2.IMREAD_GRAYSCALE)
img_low = cv2.imread(dest+"\\"+"2.jpg",cv2.IMREAD_GRAYSCALE)
img_high = cv2.resize(img_high,(320,320))
img_low = cv2.resize(img_low,(320,320))
print("shape of images:")
print("high:",img_high.shape)
print("low:",img_low.shape)

high_fft = fft.fft2(img_high)
low_fft = fft.fft2(img_low)

def pass_filter(arr,thr,val):
    M,N = arr.shape
    pass_filter = np.zeros(arr.shape)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if (i+j<=thr) or (M-i+j<=thr) or (i+N-j<=thr) or (M-i+N-j<=thr):
                pass_filter[i][j] = val
            else:
                pass_filter[i][j] = 1 - val

    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            arr[i][j] *= pass_filter[i][j]
            
    return arr

thr = img_high.shape[0]/30
high_fft = pass_filter(high_fft,thr,0)
low_fft = pass_filter(low_fft,thr,1)
result_fft = high_fft + low_fft

img_high = fft.ifft2(high_fft)
# has numerical effect , so it might be complex number
# take real part, because imaginary part is closed to zero
img_low = fft.ifft2(low_fft)
result = fft.ifft2(result_fft)

def handle_img(freq_filt_img):
    freq_filt_img = np.abs(freq_filt_img)
    freq_filt_img = freq_filt_img.astype(np.uint8)
    return freq_filt_img

img_high = handle_img(img_high)
img_low = handle_img(img_low)
result = handle_img(result)

cv2.imwrite(dest+"\\"+"high_freq_pic.jpg",img_high)
cv2.imwrite(dest+"\\"+"low_freq_pic.jpg",img_low)
cv2.imwrite(dest+"\\"+"result.jpg",result)