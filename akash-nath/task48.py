#Task: Using amin function

import numpy as np

arr = np.arange(1, 26).reshape(5, 5) #Creating a 5x5 matrix

print(arr)
print(np.amin(arr, axis = 1)) #This prints the minimum element of axis 1