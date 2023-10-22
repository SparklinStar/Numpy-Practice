#Task: Find unique intersection

import numpy as np

#np.intersect1d() returns the sorted, unique values that are in both of the input arrays

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])

result = np.intersect1d(arr1, arr2)

print("Intersection of two arrays is : ", result)