import numpy as np
import matplotlib.pyplot as plt

def dft_matrix(N):
    W = np.exp(-2j * np.pi / N)
    return np.array([[W**(i * j) for j in range(N)] for i in range(N)])

def idft_matrix(N):
    W = np.exp(2j * np.pi / N)
    return np.array([[W**(i * j) for j in range(N)] for i in range(N)]) / N

def dft(x):
    N = len(x)
    DFT = dft_matrix(N)
    return np.dot(DFT, x), DFT

def idft(X):
    N = len(X)
    IDFT = idft_matrix(N)
    return np.dot(IDFT, X), IDFT
  
x1 = np.array([1, 2, 1, 2])
x2 = np.array([4, 3, 2, 1])
X1, DFT1 = dft(x1)
X2, DFT2 = dft(x2)
X_product = X1 * X2
x_product, IDFT = idft(X_product)
print("Twiddle factor matrix for DFT (N=4):")
print(np.round(DFT1.real, decimals=2) + 1j * np.round(DFT1.imag, decimals=2))
print("\nTwiddle factor matrix for IDFT (N=4):")
print(np.round(IDFT.real, decimals=2) + 1j * np.round(IDFT.imag, decimals=2))
print("\nX1(k) =", np.round(X1, decimals=2))
print("X2(k) =", np.round(X2, decimals=2))
print("Y(k) =", np.round(X_product, decimals=2))
print("y(n) =", np.round(x_product, decimals=2))

magnitude = np.abs(x_product)
phase = np.angle(x_product)
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.stem(magnitude)
plt.title('Magnitude of IDFT')
plt.xlabel('Sample')
plt.ylabel('Magnitude')

plt.subplot(2, 1, 2)
plt.stem(phase)
plt.title('Phase of IDFT')
plt.xlabel('Sample')
plt.ylabel('Phase (radians)')
plt.tight_layout()
plt.show()
