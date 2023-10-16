# Import the numpy library and give it the alias 'np'
import numpy as np

# 8. Create a numpy array with random integers and a specified size

# Create a numpy array 'a' with a shape of (2, 3) that contains random integers between 0 and 9 (inclusive).
a = np.random.randint(10, size=(2, 3))

# Print the content of array 'a', which contains the random integers.
print(a)

# Print the shape (dimensions) of array 'a'.
print(a, '.shape : ', a.shape)

# Print the data type of the elements in array 'a'.
print('datatype : ', a.dtype)
