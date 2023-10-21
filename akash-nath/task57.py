#Task: Create random int numpy array with specific shape

import numpy as np

arr = np.arange(np.random.randint(1, 25), np.random.randint(26, 50), 3)

reshaped_arr = arr.reshape((3, 3))

print(arr)
print(reshaped_arr)