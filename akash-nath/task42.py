#Task: Swap rows

import numpy as np

arr = np.arange(1, 26).reshape(5, 5) #Creating a 5x5 matrix to swap 1st and 2nd row

print(arr)

arr[[0, 1]] = arr[[1, 0]] #This swaps the 1st and 2nd rows

print(arr)

