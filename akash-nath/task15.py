#Task: Reshape with -1 (lazy option)
import numpy as np

arr = np.arange(1, 41)

reshaped_arr = arr.reshape(5, -1)

print(arr)

print(reshaped_arr)