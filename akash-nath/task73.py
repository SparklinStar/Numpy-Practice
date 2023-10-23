#Task: array vs asarray

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

list1 = arr.tolist() #Convert the array to a list

arr1 = np.asarray(list1) #Convert the list to an array

print(list1)
print(arr1)