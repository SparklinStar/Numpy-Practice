#Task: Find common values between two numpy array

import numpy as np

#To determine the common values between two numpy array, we can use np.intersect1d() function

arr1 = np.arange(1, 7)
arr2 = np.arange(3, 10)

common_values = np.intersect1d(arr1, arr2)

print(common_values) #Should print an array containing all the common elements.