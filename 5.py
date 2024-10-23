 #Rectangular window 
import numpy as np  
import matplotlib.pyplot as plt 
n= np.array([1,2,3,4]) 
hdn = (np.sin(np.pi/4) *(n-2)) / (np.pi * ( n-2)) 
wn = np.ones_like(n) 
hn = np.array([1,3,0.25,0]) 
print (hn) 
plt.subplot(4,1,1) 
plt.stem(n,hn) 
plt.xlabel('n') 
plt.ylabel('h(n)') 
plt.title('Rectangular  window response') 
plt.grid(True) 
plt.show()
 
#Hanning window 
import numpy as np 
import matplotlib.pyplot as plt 
n = np.arange(0 , 5) 
hdn = (np.sin((np.pi / 4) * (n - 2))) / (np.pi * (n - 2)) 
wn = 0.5 - 0.5 * np.cos(2 * np.pi * n / 4)  
hn = hdn * wn 
hn[1] = 0.25 
plt.figure() 
plt.subplot(4,1,3) 
plt.plot(n, hn) 
plt.xlabel('n') 
plt.ylabel('hi(n)') 
plt.title('Hanning Window Response') 
plt.grid(True) 
plt.show() 

#Blackman window 
import numpy as np
import matplotlib.pyplot as plt 
n = np.array([0,1,2,3,4]) 
hdn = (np.sin(np.pi / 4) * (n - 2)) / (np.pi * (n - 2)) 
hdn[2]=0.25 
wn = 0.42-0.5*np.cos(2* np.pi*n/ 4)+0.08*np.cos(4*np.pi*n/4) 
hn = hdn* wn 
hn[1]=hn[3]=0.25 
print (hn) 
plt.subplot(4,1,2) 
plt.stem(n,hn) 
plt.xlabel('n') 
plt.ylabel('h(n)') 
plt.title('Hamming  window response') 
plt.grid(True) 
plt.show() 

#Hamming Window 
import numpy as np 
import matplotlib.pyplot as plt 
n = np.array([0,1,2,3,4]) 
hdn = (np.sin(np.pi / 4) * (n - 2)) / (np.pi * (n - 2)) 
hdn[2]=0.25 
wn = 0.54 -0.46*np.cos(2* np.pi*n/ 4)  
hn = hdn* wn 
print (hn) 
plt.subplot(4,1,2) 
plt.stem(n,hn) 
plt.xlabel('n') 
plt.ylabel('h(n)') 
plt.title('Hamming  window response') 
plt.grid(True) 
plt.show() 

