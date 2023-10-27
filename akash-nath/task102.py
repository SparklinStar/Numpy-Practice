#Task: Array Append on Axis 0 and Axis 1

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr)
new_arr = np.append(arr, [[7, 8, 9]], axis=0)
print(new_arr)
new_arr = np.append(arr, [[5, 5, 5], [7, 8, 9]], axis=1)
print(new_arr)