import numpy as np

# Create a NumPy array containing 10000 elements
x = np.arange(10000)

# Print the array before setting print options (will be truncated by default)
print('Before setting print options : ')
print(x)

# Import the sys module for sys.maxsize (maximum integer value supported by your system)
import sys

# Set the print options to prevent truncation by setting the threshold to the maximum integer value
np.set_printoptions(threshold=sys.maxsize)

# Print the array again after setting the new print options (will not be truncated)
print('\nAfter setting print options : ')
print(x)
