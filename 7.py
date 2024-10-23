#IIR filter 
import numpy as np  
from scipy import signal 
ohm=4 
wc=np.pi/2 
T=2*np.tan(wc/2)/ohm 
fs=1/T 
n=np.array([1,0.1]) 
d=np.array([1,0.2,16.01]) 
Nr,Dr=signal.bilinear(n,d,fs) 
print("Nr:",Nr, "\nDr:",Dr) 

#part 2 
import numpy as np  
from scipy import signal 
ohm=4 
wc=np.pi/2 
T=2*np.tan(wc/2)/ohm 
fs=1/T 
n=np.array([1,0.1]) 
d=np.array([1,0.2,9.01]) 
Nr,Dr=signal.bilinear(n,d,fs) 
print("Nr:",Nr, "\nDr:",Dr) 
