import numpy as np
import matplotlib.pyplot as plt
# Parameters
n = np.arange(0, 20)  # Discrete time array (0 to 19)
signal = np.sin(0.2 * np.pi * n)  # Example discrete-time signal (sine wave)
# Delay the signal by 3 samples
delay = 3
delayed_signal = np.zeros_like(signal)
delayed_signal[delay:] = signal[:-delay]
# Advance the signal by 3 samples
advance = 3
advanced_signal = np.zeros_like(signal)
advanced_signal[:-advance] = signal[advance:]
# Plot the original and shifted signals
plt.figure(figsize=(12, 8))
# Original Signal
plt.subplot(3, 1, 1)
plt.stem(n, signal, use_line_collection=True)
plt.title('Original Signal')
plt.xlabel('n (Discrete Time)')
plt.ylabel('Amplitude')
# Delayed Signal
plt.subplot(3, 1, 2)
plt.stem(n, delayed_signal, use_line_collection=True)
plt.title(f'Delayed Signal (by {delay} samples)')
plt.xlabel('n (Discrete Time)')
plt.ylabel('Amplitude')
# Advanced Signal
plt.subplot(3, 1, 3)
plt.stem(n, advanced_signal, use_line_collection=True)
plt.title(f'Advanced Signal (by {advance} samples)')
plt.xlabel('n (Discrete Time)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()