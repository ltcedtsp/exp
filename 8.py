import numpy as np 
from scipy.signal import butter, lfilter 
import matplotlib.pyplot as plt 

input_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
Fs = 1000  
Fc = 50    
N = 4      

Wn = Fc / (Fs / 2)  
b, a = butter(N, Wn, btype='high', analog=False) 
filtered_sequence = lfilter(b, a, input_sequence) 
t = np.arange(len(input_sequence)) / Fs 

plt.figure(figsize=(12, 8))  
plt.subplot(2, 1, 1) 
plt.plot(t, input_sequence, 'bo-', label='Original Sequence') 
plt.title('Original Sequence') 
plt.xlabel('Time [s]') 
plt.ylabel('Amplitude') 
plt.grid(True) 
plt.legend() 

plt.subplot(2, 1, 2) 
plt.plot(t, filtered_sequence, 'ro-', label='Filtered Sequence') 
plt.title('Filtered Sequence (High-Pass Butterworth)') 
plt.xlabel('Time [s]') 
plt.ylabel('Amplitude') 
plt.grid(True) 
plt.legend() 
plt.tight_layout() 
plt.show() 
