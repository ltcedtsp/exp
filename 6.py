import numpy as np
N = 5  
hn = []

for n in range(1, N + 1):
    hdn = (1 / (np.pi * n)) * (np.sin(np.pi * n) - np.sin((np.pi * n) / 4))
    wn = (0.54 + 0.46 * np.cos(np.pi * n / 5))
    hn_value = wn * hdn
    hn.append(hn_value)

hn_array = np.array(hn)
print("High-Pass FIR Filter Coefficients:")
print(hn_array)

