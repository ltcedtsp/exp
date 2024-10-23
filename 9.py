# Decimation Process 
import numpy as np 
import matplotlib.pyplot as plt 

xn = np.array([1, -1, 1, -1, 2, -2, 2, -2, 3, -3, 3, -3]) 
N = len(xn) 
n = np.arange(N) 

xD2n = xn[::2] 
n1 = np.arange(len(xD2n)) 
xD3n = xn[::3] 
n2 = np.arange(len(xD3n)) 

plt.figure(figsize=(10, 8)) 
plt.subplot(3, 1, 1) 
plt.stem(n, xn, 'k')
plt.xlabel('n', fontsize=11, fontweight='bold') 
plt.ylabel('x(n)', fontsize=11, fontweight='bold') 
plt.title('Signal x(n)', fontsize=11, fontweight='bold') 
plt.grid(True) 

plt.subplot(3, 1, 2) 
plt.stem(n1, xD2n, 'k') 
plt.xlabel('n', fontsize=11, fontweight='bold') 
plt.ylabel('x_D_2(n)', fontsize=11, fontweight='bold') 
plt.title('Downsampled Signal, D=2', fontsize=11, fontweight='bold') 
plt.grid(True) 

plt.subplot(3, 1, 3) 
plt.stem(n2, xD3n, 'k')  
plt.xlabel('n', fontsize=11, fontweight='bold') 
plt.ylabel('x_D_3(n)', fontsize=11, fontweight='bold') 
plt.title('Downsampled Signal, D=3', fontsize=11, fontweight='bold') 
plt.grid(True) 

plt.tight_layout() 
plt.show()
