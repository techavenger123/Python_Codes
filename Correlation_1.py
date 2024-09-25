import numpy as np
import matplotlib.pyplot as plt

# Define two signals
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

# Perform cross-correlation using numpy
cross_corr = np.correlate(x, y, mode='full')

# Plot cross-correlation
plt.stem(cross_corr)
plt.title('Cross-Correlation')
plt.show()
