#Task: Array of NaN

import numpy as np

#Making an array of NaN can be done in two methods
#Method: 1
arr = np.array([np.nan, np.nan, np.nan])
print(arr)

#Method: 2
shape = (3,3)
arr = np.full(shape, np.nan)
print(arr)