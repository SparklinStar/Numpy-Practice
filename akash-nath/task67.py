#Task: Trying to inverse a singular matrix

import numpy as np

#np.linalg.inv() computes the (multiplicative) inverse of a matrix

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(arr)

try:
    print(np.linalg.inv(arr))
except np.linalg.LinAlgError:
    print("The matrix is a singular matrix and hence cannot be inverted")