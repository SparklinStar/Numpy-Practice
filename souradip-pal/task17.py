# 17. Numpy with precision 
import numpy as np  # Import the NumPy library
# Generate an array of 10 random floating-point numbers between 0 and 1
x = np.random.random(10)

# Print the original array
print('Original Array:')
print(x)

# Set the precision for printing floating-point numbers to 2 decimal places
print('\nAfter setting precision:')
np.set_printoptions(precision=2)
print(x)

# Resetting the precision to the default (8 decimal places)
np.set_printoptions(precision=8)
