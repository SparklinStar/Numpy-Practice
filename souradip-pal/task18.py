import numpy as np  # Import the NumPy library

# 18. Argsort on Numpy array 

# Create a 3x3 NumPy array filled with random integers from 0 to 9
a = np.random.randint(0, 10, (3, 3))
print('Before : ')
print(a)

# Sort the array 'a' based on the values in the third column (column index 2).
# This is done using argsort, which returns the indices that would sort the array.
# Then, these indices are used to rearrange the rows of the original array.
# As a result, 'b' will contain the rows of 'a' sorted in ascending order of the third column.
print('\nAfter : ')
b = a[a[:, 2].argsort()]
print(b)
