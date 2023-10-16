#Task: Count elements of an array

import numpy as np

arr = np.array([1, 10, 55, 100])

#Method 1:
print(len(arr))

#Method 2:
print(arr.size)

#Method 3: (Does't work for '0')
print(np.count_nonzero(arr))
