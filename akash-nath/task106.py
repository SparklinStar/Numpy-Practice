#Task: Continguous Array

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Check if arr is contiguous
contiguous_arr = np.ascontiguousarray(arr)

print(contiguous_arr.flags)
