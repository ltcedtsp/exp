# Take numerator and denominator from user (input= numerator 3 , denominator 1 -0.166 -0.166)
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

b = list(map(float, input("Enter the numerator coefficients (space-separated): ").split()))
a = list(map(float, input("Enter the denominator coefficients (space-separated): ").split()))
w, h = freqz(b, a)

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(w / np.pi, 20 * np.log10(abs(h))) 
plt.grid(True)
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.title('Magnitude Response')

plt.subplot(2, 1, 2)
plt.plot(w / np.pi, np.angle(h)) 
plt.grid(True)
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Phase (radians)')
plt.title('Phase Response')
plt.tight_layout()
plt.show()

# finding /compute the sequence and sketch amplitude/phase 
import numpy as np
import matplotlib.pyplot as plt

W = np.arange(0, 2 * np.pi, np.pi / 200)
H = np.exp(-1j * 5 * W) * 2 * np.cos(5 * W)

plt.subplot(2, 1, 1)
plt.plot(W, np.abs(H))
plt.axis([0, 2 * np.pi, 0, np.max(np.abs(H))])
plt.grid(True)
plt.ylabel('Magnitude')

plt.subplot(2, 1, 2)
plt.plot(W, np.angle(H))
plt.axis([0, 2 * np.pi, -np.pi, np.pi])
plt.grid(True)
plt.ylabel('Phase (radians)')
plt.xlabel('Frequency (rad/sample)')
plt.tight_layout()
plt.show()

