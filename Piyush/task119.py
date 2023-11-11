import numpy as np
import numpy.ma as ma

arr = np.array([1, 2, 3])
masked_arr = ma.masked_array(arr, mask=False)

# Attempt to modify the masked array will not affect the original array
masked_arr[0] = 4

print(arr)  # Original array is unchanged
#end of task119
