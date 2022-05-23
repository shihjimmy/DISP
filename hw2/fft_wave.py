import numpy as np
from os import path
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import wave
import simpleaudio as sa

"""
    trying to convert the digital(discrete) signal back to the original one
    by using the DFT && FT relation
    testing via checking before & after spectrum
"""

file_path = path.dirname(__file__)
file_path = path.join(file_path,"sample.wav")  

# get the wave file(discrete)
wavefile = wave.open(file_path,'rb')  # rb for only read && wb for only write
fs = wavefile.getframerate()   # sampling frequency 
num_frame = wavefile.getnframes()  # length of the vocal signal -> total number of the sampling points
n_channel = wavefile.getnchannels() # channels of wavefile
delta_t = 1/fs  # sampling intervals

str_data = wavefile.readframes(num_frame) # return <class bytes> (a class in python)
wave_data = np.frombuffer(str_data, dtype=np.int16) # turn bytes into np array with integers
wave_data = np.reshape(wave_data,(num_frame,n_channel))  #reshape the ndarray if it is  2-channel

""" 
    After doing the discrete fourier transform
    Before drawing the spectrum 
    need to move the 1/2 spectrum to the front
    to get the original spectrum
"""
fft_data = abs(fft(wave_data[:,1]))*delta_t
n0 = int(np.ceil(num_frame/2))
fft_data1 = np.concatenate([fft_data[n0:num_frame],fft_data[0:n0]])  
freq = np.concatenate([range(n0-num_frame,0),range(0,n0)]) * fs / num_frame
# since we move half spectrum to the front
# we need to move the freq axis ,too
plt.plot(freq,fft_data1,label = "frequency")
plt.xlim(-1000,1000)
plt.show()
