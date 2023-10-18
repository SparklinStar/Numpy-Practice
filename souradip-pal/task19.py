# Import the NumPy library
import numpy as np

# 19. Numpy view

# Create a structured NumPy array with two fields 'a' and 'b', both of type np.int8
x = np.array([(1, 2)], dtype=[('a', np.int8), ('b', np.int8)])
print(x)  # Display the original array
print(x.dtype)  # Display the data type of the original array

# Create a new view of the array 'x' with a different data type (np.int16)
y = x.view(dtype=np.int16, type=np.matrix)
print(y)  # Display the new view 'y'
print(y.dtype)  # Display the data type of the new view 'y'
