#Task: Random array and sorting

import numpy as np

#We can sort an array with according to an axis using np.sort() function

arr = np.random.rand(1, 100)

sorted_arr = np.sort(arr, axis=1)

print(arr)
print(sorted_arr)