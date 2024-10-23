# DFT Using DIT FFT 
import numpy as np
import matplotlib.pyplot as plt

print("Enter the sequence:")
x0 = complex(input("x(0)="))
x1 = complex(input("x(1)="))
x2 = complex(input("x(2)="))
x3 = complex(input("x(3)="))
x4 = complex(input("x(4)="))
x5 = complex(input("x(5)="))
x6 = complex(input("x(6)="))
x7 = complex(input("x(7)="))

# Stage 1
a = x0 + x4
b = x0 - x4
c = x2 + x6
d = x2 - x6
e = x1 + x5
f = x1 - x5
g = x3 + x7
h = x3 - x7

# Stage 2
i = a + np.exp(-2j * np.pi * 0 / 8) * c
j = b + np.exp(-2j * np.pi * 2 / 8) * d
k = a - np.exp(-2j * np.pi * 0 / 8) * c
l = b - np.exp(-2j * np.pi * 2 / 8) * d
m = e + np.exp(-2j * np.pi * 0 / 8) * g
n = f + np.exp(-2j * np.pi * 2 / 8) * h
o = e - np.exp(-2j * np.pi * 0 / 8) * g
p = f - np.exp(-2j * np.pi * 2 / 8) * h

# Stage 3
X0 = i + np.exp(-2j * np.pi * 0 / 8) * m
X1 = j + np.exp(-2j * np.pi * 1 / 8) * n
X2 = k + np.exp(-2j * np.pi * 2 / 8) * o
X3 = l + np.exp(-2j * np.pi * 3 / 8) * p
X4 = i - np.exp(-2j * np.pi * 0 / 8) * m
X5 = j - np.exp(-2j * np.pi * 1 / 8) * n
X6 = k - np.exp(-2j * np.pi * 2 / 8) * o
X7 = l - np.exp(-2j * np.pi * 3 / 8) * p

X = np.array([X0, X1, X2, X3, X4, X5, X6, X7])
print("X[K] =", X)

# Calculate magnitudes
magnitudes = np.abs(X)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.stem(magnitudes)
plt.title('Magnitude of X')
plt.xlabel('Index')
plt.ylabel('Magnitude')

plt.subplot(1, 2, 2)
plt.stem(np.real(X))
plt.title('Pulse Graph of X (Real Part)')
plt.xlabel('Index')
plt.ylabel('Real Part')
plt.tight_layout()
plt.show()

# IDFT Using DIT FFT
import numpy as np
import matplotlib.pyplot as plt

print("Enter the sequence:")
x0 = complex(input("x(0)="))
x1 = complex(input("x(1)="))
x2 = complex(input("x(2)="))
x3 = complex(input("x(3)="))
x4 = complex(input("x(4)="))
x5 = complex(input("x(5)="))
x6 = complex(input("x(6)="))
x7 = complex(input("x(7)="))

# Stage 1
a = x0 + x4
b = x0 - x4
c = x2 + x6
d = x2 - x6
e = x1 + x5
f = x1 - x5
g = x3 + x7
h = x3 - x7

# Stage 2
i = a + np.exp(-2j * np.pi * 0 / 8) * c
j = b + np.exp(-2j * np.pi * 2 / 8) * d
k = a - np.exp(-2j * np.pi * 0 / 8) * c
l = b - np.exp(-2j * np.pi * 2 / 8) * d
m = e + np.exp(-2j * np.pi * 0 / 8) * g
n = f + np.exp(-2j * np.pi * 2 / 8) * h
o = e - np.exp(-2j * np.pi * 0 / 8) * g
p = f - np.exp(-2j * np.pi * 2 / 8) * h

# Stage 3
X0 = i + np.exp(-2j * np.pi * 0 / 8) * m
X1 = j + np.exp(-2j * np.pi * 1 / 8) * n
X2 = k + np.exp(-2j * np.pi * 2 / 8) * o
X3 = l + np.exp(-2j * np.pi * 3 / 8) * p
X4 = i - np.exp(-2j * np.pi * 0 / 8) * m
X5 = j - np.exp(-2j * np.pi * 1 / 8) * n
X6 = k - np.exp(-2j * np.pi * 2 / 8) * o
X7 = l - np.exp(-2j * np.pi * 3 / 8) * p

X = np.array([X0, X1, X2, X3, X4, X5, X6, X7])
print("X[K] =", X)

# Calculate magnitudes
magnitudes = np.abs(X)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.stem(magnitudes)
plt.title('Magnitude of X')
plt.xlabel('Index')
plt.ylabel('Magnitude')

plt.subplot(1, 2, 2)
plt.stem(np.real(X))
plt.title('Pulse Graph of X (Real Part)')
plt.xlabel('Index')
plt.ylabel('Real Part')
plt.tight_layout()
plt.show()


