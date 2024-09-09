import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
fs = 500  # Sampling frequency
f = 5  # Frequency of the signal
t = np.linspace(0, 1, fs, endpoint=False)  # Time array
# Create a triangular wave signal using scipy
triangular_wave = signal.sawtooth(2 * np.pi * f * t, 0.5)
# Create a ramp (sawtooth) signal using scipy
ramp_signal = signal.sawtooth(2 * np.pi * f * t)
# Plot the signals
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(t, triangular_wave)
plt.title('Triangular Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(2, 1, 2)
plt.plot(t, ramp_signal)
plt.title('Ramp Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()