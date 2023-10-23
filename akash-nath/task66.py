#task: Find the diff

import numpy as np

#np.setdiff1d() returns the sorted, unique values in arr1 that are not in arr2
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])

print(np.setdiff1d(arr1, arr2))