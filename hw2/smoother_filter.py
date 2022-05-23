import numpy as np
import random
import math
from os import path
import matplotlib.pyplot as plt
from scipy import signal

np.random.seed(0)
noise = (np.random.rand(152)-0.5)
destination = path.join(path.dirname(__file__),"smooth_filter_results")
wave = np.ndarray(152)
L = 151
wave[0] = 0
for i in range(1,152):
    wave[i] = 0.1 * (i-50-1)

def edge_detection(sigma,an,l):
    
    sum = 0
    for i in range(L):
        sum+=math.exp(-1*sigma*i)
    C = 1/(2*sum)
    imp_response = np.ndarray(L*2+1)
    for i in range(1,imp_response.shape[0]):
        imp_response[i] = C *  math.exp(-1*sigma*abs(i-L-1))
    
    wave_noise = wave + an*noise
    return signal.convolve(wave_noise,imp_response,mode = "same") # keep the signal length same

def draw_plt(arr,file_path,s):
    n = np.ndarray(arr.shape)
    for i in range(arr.shape[0]):
        n[i] = i - 51
    plt.plot(n,arr)
    plt.savefig(destination+"//"+s)
    plt.close()
    
# original and edge_detection results
draw_plt(wave,destination,"original")
draw_plt((wave+noise),destination,"original_with_noise")
for sgm in range(1,6):
    for an in range(1,6):
       draw_plt(edge_detection(sgm/10,an,L),destination,str(sgm)+" "+str(an))