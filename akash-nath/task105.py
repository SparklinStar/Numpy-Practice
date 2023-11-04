#Task: Transpose

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr)

#Transposing an array interchanges the row and columns of the array
new_arr = np.transpose(arr)

print(new_arr)
