# 16. Reshape with -1 (lazy option)
import numpy as np  # Import the NumPy library
# Create a 3x4 matrix
a = np.matrix([[1, 2, 3, 4], [5, 6, 7, 8], [10, 11, 12, 21]])

# Print the original numpy array
print('Original Numpy Array:')
print(a)
print('Original shape:', a.shape)

# Reshape the array using -1 to determine the size along that axis automatically
c = np.reshape(a, -1)

# Print the result and the new shape
print('\nnp.reshape(a, -1):')
print(c)
print('New shape:', c.shape)

# Reshape the array into a 1xN array (1D)
d = np.reshape(a, (1, -1))

# Print the result and the new shape
print('\nnp.reshape(a, (1, -1)):')
print(d)
print('New shape:', d.shape)

# Reshape the array into a 2xN array, where N is determined automatically
e = np.reshape(a, (2, -1))

# Print the result and the new shape
print('\nnp.reshape(a, (2, -1)):')
print(e)
print('New shape:', e.shape)

# Reshape the array into a 3xN array, where N is determined automatically
f = np.reshape(a, (3, -1))

# Print the result and the new shape
print('\nnp.reshape(a, (3, -1)):')
print(f)
print('New shape:', f.shape)

# Reshape the array into a 4xN array, where N is determined automatically
g = np.reshape(a, (4, -1))

# Print the result and the new shape
print('\nnp.reshape(a, (4, -1)):')
print(g)
print('New shape:', g.shape)
