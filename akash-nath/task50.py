#Task: Get min of axis = 0

import numpy as np

arr = np.arange(1, 26).reshape(5, 5) #Creating a 5x5 matrix

print(arr)
print(np.min(arr, axis = 0)) #This prints the minimum element of axis 0