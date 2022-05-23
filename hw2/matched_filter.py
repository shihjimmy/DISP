import numpy as np
import random
import math
from os import path
import matplotlib.pyplot as plt
from scipy import signal

# setting the input signal and the desired pattern
input_wave = np.ndarray(40)
input_wave[0] = input_wave[1] = input_wave[7] = input_wave[8] = input_wave[16] = input_wave[17] = 0
input_wave[25] = input_wave[26] = input_wave[36] = input_wave[37] = input_wave[38] = input_wave[39] = 0
for i in range(2,7):
    input_wave[i] = 3
for i in range(9,16):
    input_wave[i] = (-3+(i-9))
for i in range(18,25):
    input_wave[i] = (3-(i-18))
for i in range(9):
    input_wave[i+27] = math.sin(i * math.pi/4)
    
desired_wave = np.ndarray(13)
desired_wave[0] = desired_wave[1] = desired_wave[10] = desired_wave[11] = desired_wave[12] = 0
for i in range(8):
    # h[n] != 0 for n=2 to 9
    desired_wave[i+2] = (-3+i)
    
# print the original wave and the desired_wave
def plot_signal(arr, file_path,s):
    n = np.arange(arr.shape[0])
    plt.plot(n,arr)
    plt.savefig(file_path+"//"+s)
    plt.close()

plot_signal(input_wave, path.join(path.dirname(__file__),"matched_filter_results"), "original_signal")
plot_signal(desired_wave, path.join(path.dirname(__file__),"matched_filter_results"), "desired_pattern")

# To detect a pattern h[n], we use its time-reverse and conjugation form as the filter
for i in range(6):
    temp = desired_wave[i]
    desired_wave[i] = desired_wave[12-i]
    desired_wave[12-i] = temp
     
desired_filter = np.conj(desired_wave)
plot_signal(desired_wave, path.join(path.dirname(__file__),"matched_filter_results"), "desired_filter")

result = signal.convolve(input_wave,desired_filter, mode = "same")
plot_signal(result, path.join(path.dirname(__file__),"matched_filter_results"), "result_before_normalized")

sum_1 = 0
for i in range(input_wave.shape[0]):
    sum_1 += input_wave[i]*input_wave[i]
sum_2 = 0
for i in range(desired_wave.shape[0]):
    sum_2 += desired_wave[i]*desired_wave[i]

result /= math.sqrt(sum_1 * sum_2)
for i in range(input_wave.shape[0]):
    if input_wave[i]==0 :
        result[i] = 0
plot_signal(result, path.join(path.dirname(__file__),"matched_filter_results"), "result_after_normalized")