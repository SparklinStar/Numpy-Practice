#Task: Numpy Reshape with Order

import numpy as np

arr = np.arange(8)
print(arr)

#Reshape the array with order C
new_arr = np.reshape(arr, (2, 4), order='C')

print(new_arr)