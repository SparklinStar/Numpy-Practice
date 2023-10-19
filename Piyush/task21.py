import numpy as np

# Create a sample square matrix
a = np.array([[10, 25],
              [35, 45]])

# Compute the inverse of the matrix
a_inv = np.linalg.inv(a)

# Print the original matrix and its inverse
print("original Matrix:")
print(a)
print("\n inverse Matrix:")
print(a_inv)
