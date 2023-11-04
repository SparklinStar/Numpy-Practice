#Task: Rearrange array with specified index

import numpy as np

arr = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19])

new_arr = np.array([arr[6], arr[7], arr[8], arr[3], arr[4], arr[5], arr[0], arr[1], arr[2]]) #Rearranging array

print(arr)
print(new_arr)