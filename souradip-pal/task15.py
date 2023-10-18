# 15. Get the nth column of an array

import numpy as np

# Create a NumPy array 'x' with three rows and two columns
x = np.array([[1, 2], [3, 4], [5, 6]])

# Print the original NumPy array 'x'
print('Numpy array:')
print(x)

# Extract the first column (column at index 0) and store it in 'y'
y = x[:, 0]

# Print the first column 'y'
print('\nx[:,0]:')
print(y)

# Extract the second column (column at index 1) and store it in 'z'
z = x[:, 1]

# Print the second column 'z'
print('\nx[:, 1]:')
print(z)

# Extract the second row (row at index 1) and store it in 'a'
a = x[1, :]

# Print the second row 'a'
print('\nx[1,:]:')
print(a)
