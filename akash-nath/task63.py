#Task: Get unique elements

import numpy as np

#np.unique() returns the sorted unique elements (without repeating them) of an array

arr = np.array([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
unique_elements = np.unique(arr)

print(arr)
print(unique_elements)