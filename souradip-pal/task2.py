# Import the numpy library and give it the alias 'np'
import numpy as np

# 2. Check whether the array is empty

# Create an empty 2x2 array filled with uninitialized integers
empty_array = np.empty([2, 2], int)

# Print the content of the empty_array
print(empty_array)

# Print the shape (dimensions) of the empty_array
print(empty_array.shape)

# Print the total number of elements in the empty_array
print(empty_array.size)
