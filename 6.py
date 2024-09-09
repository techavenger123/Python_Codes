import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# Parameters
fs = 500  # Sampling frequency
t = np.linspace(-1, 1, fs, endpoint=False)  # Time array
# 1. Unit Step Signal
unit_step = np.heaviside(t, 1)
# 2. Unit Impulse Signal (Dirac Delta)
unit_impulse = np.zeros_like(t)
unit_impulse[fs//2] = 1  # Impulse at t=0
# 3. Ramp Signal
ramp_signal = signal.sawtooth(2 * np.pi * t, 1)
# 4. Sine Wave
f_sine = 5  # Frequency of the sine wave
sine_wave = np.sin(2 * np.pi * f_sine * t)
# 5. Cosine Wave
f_cosine = 5  # Frequency of the cosine wave
cosine_wave = np.cos(2 * np.pi * f_cosine * t)
# 6. Exponential Signal
exponential_signal = np.exp(t)
# 7. Triangular Wave
triangular_wave = signal.sawtooth(2 * np.pi * 5 * t, 0.5)
# 8. Square Wave
square_wave = signal.square(2 * np.pi * 5 * t)
# Plot the signals
plt.figure(figsize=(12, 12))
plt.subplot(4, 2, 1)
plt.plot(t, unit_step)
plt.title('Unit Step Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(4, 2, 2)
plt.plot(t, unit_impulse)
plt.title('Unit Impulse Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(4, 2, 3)
plt.plot(t, ramp_signal)
plt.title('Ramp Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(4, 2, 4)
plt.plot(t, sine_wave)
plt.title('Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(4, 2, 5)
plt.plot(t, cosine_wave)
plt.title('Cosine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(4, 2, 6)
plt.plot(t, exponential_signal)
plt.title('Exponential Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(4, 2, 7)
plt.plot(t, triangular_wave)
plt.title('Triangular Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(4, 2, 8)
plt.plot(t, square_wave)
plt.title('Square Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()