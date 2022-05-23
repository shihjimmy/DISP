import numpy as np
import random
import math
from os import path
import matplotlib.pyplot as plt
from scipy import signal

np.random.seed(0)
noise = (np.random.rand(132)-0.5)
destination = path.join(path.dirname(__file__),"edge_filter_results")
wave = np.ndarray(132)
L = 131
wave[0] = 0
for i in range(1,132):
    if (i >=21 and i<=51) or (i>=81 and i<=111):
        wave[i] = 1
    elif (i>=1 and i< 21) or (i>51 and i<81) or (i>111 and i<=131):
        wave[i] = 0

def edge_detection(sigma,an,l):
    def sign_func(m,L):
        n = m - L - 1
        if n==0:
            return 0
        elif n>0:
            return 1
        else:
            return -1 
    sum = 0
    for i in range(L):
        sum+=math.exp(-1*sigma*i)
    C = 1/sum
    imp_response = np.ndarray(131*2+3)
    for i in range(1,imp_response.shape[0]):
        imp_response[i] = C * sign_func(i,L) * math.exp(-1*sigma*abs(i-L-1))
    
    wave_noise = wave + an*noise
    return signal.convolve(wave_noise,imp_response,mode = "same") # keep the signal length same

def draw_plt(arr,file_path,s):
    n = np.ndarray(arr.shape)
    for i in range(arr.shape[0]):
        n[i] = i - arr.shape[0]/2
    plt.plot(n,arr)
    plt.savefig(destination+"//"+s)
    plt.close()
    
# original and edge_detection results
draw_plt(wave,destination,"original")
draw_plt((wave+noise),destination,"original_with_noise")
for sgm in range(1,6):
    for an in range(1,6):
        draw_plt(edge_detection(sgm/10,an,L),destination,str(sgm)+" "+str(an))