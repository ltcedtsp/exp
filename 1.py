#DFT OF GIVEN SEQUENCE EXP-1 
import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, -2+2j, 3+1j, 1])
N = len(x)
X = np.zeros(N, dtype=complex)

for k in range(N):
    for n in range(N):
        X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)

print("Input sequence is:")
print(x)
print("DFT of x(n) is :")
print(X)
magnitude_spectrum = np.abs(X)
plt.stem(np.arange(N), magnitude_spectrum)
plt.title('Magnitude Spectrum of DFT')
plt.xlabel('Frequency Index (k)')
plt.ylabel('Magnitude')
plt.xticks(np.arange(N))
plt.grid(True)
plt.show()

phase_spectrum = np.angle(X)
plt.stem(np.arange(N), phase_spectrum)
plt.title('Phase Spectrum of DFT')
plt.xlabel('Frequency Index (k)')
plt.ylabel('Phase (radians)')
plt.xticks(np.arange(N))
plt.grid(True)
plt.show()

# IDFT OF GIVEN SEQUENCE EXP-1 
import numpy as np
import matplotlib.pyplot as plt

X = np.array([2, -2 + 2j, 3 + 1j, 1])
N = len(X)
x = np.zeros(N, dtype=complex)

for n in range(N):
    for k in range(N):
        x[n] += X[k] * np.exp(2j * np.pi * k * n / N)
    x[n] /= N
print("Input sequence is:")
print(X)
print("\nIDFT of x(n) is:")
print(x)

magnitude_spectrum = np.abs(x)
plt.stem(np.arange(N), magnitude_spectrum)
plt.title('Magnitude Spectrum of IDFT')
plt.xlabel('Frequency Index (k)')
plt.ylabel('Magnitude')
plt.xticks(np.arange(N))
plt.grid(True)
plt.show()

phase_spectrum = np.angle(x)
plt.stem(np.arange(N), phase_spectrum)
plt.title('Phase Spectrum of IDFT')
plt.xlabel('Frequency Index (k)')
plt.ylabel('Phase (radians)')
plt.xticks(np.arange(N))
plt.grid(True)
plt.show()

