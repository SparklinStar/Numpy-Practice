#Task: Shuffle

import numpy as np

arr = np.arange(1, 26).reshape(5, 5) #Creating a 5x5 matrix to shuffle the rows
print(arr)

np.random.shuffle(arr) #This shuffles the rows of the matrix
print(arr)