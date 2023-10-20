#Task: Min, Max, Sum

import numpy as np

arr = np.arange(1, 26).reshape(5, 5) #Creating a 5x5 matrix

print(arr)
print(np.min(arr)) #This prints the minimum element of the matrix
print(np.max(arr)) #This prints the maximum element of the matrix
print(np.sum(arr)) #This prints the sum of all the elements of the matrix