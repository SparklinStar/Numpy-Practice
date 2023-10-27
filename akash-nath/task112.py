#Task: Immutable Array

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Make arr immutable

immutable_arr = np.array([1, 2, 3, 4, 5])
immutable_arr.flags.writeable = False #Makes the array readonly. When the array is getting written, it throws error
immutable_arr[0] = 2 #Will raise an error

print(immutable_arr)