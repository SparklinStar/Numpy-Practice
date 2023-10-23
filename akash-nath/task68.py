#Task: Find the union

import numpy as np

#np.union1d() returns the sorted, unique values that are in either of the two input arrays

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])

print(np.union1d(arr1, arr2))