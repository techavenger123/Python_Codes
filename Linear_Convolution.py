import numpy as np
# Define two input signals
x = [1, 2, 3, 4]
h = [1, 0, -1]
# Perform linear convolution using numpy
linear_conv = np.convolve(x, h)
print("Linear Convolution: ", linear_conv) 
