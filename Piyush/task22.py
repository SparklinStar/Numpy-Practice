import numpy as np

a = np.array([[25, 15],
              [75, 45]])

a_inv = np.linalg.inv(a)

# Print the original matrix and its inverse
print("Original Matrix:")
print(a)
print("\nInverse Matrix:")
print(a_inv)
#end of 22
