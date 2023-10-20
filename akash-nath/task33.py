#Task: List to numpy array

import numpy as np

pythonList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

arr = np.array(pythonList)

reshaped_arr = arr.reshape((3, 3))

print(pythonList)
print(arr)
print(reshaped_arr)