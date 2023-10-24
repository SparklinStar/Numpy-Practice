#Task: Numpy Concatenate

import numpy as np

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])

arr3 = np.concatenate((arr1,arr2),axis=0) #axis=0 means row wise concatenation
arr4 = np.concatenate((arr1,arr2),axis=1) #axis=1 means column wise concatenation

print(arr3)
print(arr4)