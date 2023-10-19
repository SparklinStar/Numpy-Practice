#Task: List to numpy array with explicit dtype

import numpy as np

#Explicit dtype specifies the datatype should be taken. In this case, it specifies that only a specific datatype will be accepted for the array

pythonList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

arr = np.array(pythonList, dtype=np.int32)

reshaped_arr = arr.reshape((3, 3))

print(pythonList)
print(arr)
print(reshaped_arr)