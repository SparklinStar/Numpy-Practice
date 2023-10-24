#Task: Ravel vs. Flatten

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

raveled_arr = arr.ravel() #Ravel changes the main array
raveled_arr[0] = 99

flattened_arr = arr.flatten() #Flatten creates a new array first and then changes in the new array
flattened_arr[1] = 88

print(arr)
print(raveled_arr)
print(flattened_arr)
print(arr)
