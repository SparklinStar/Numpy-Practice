#Task: Set Error in Numpy

import numpy as np

np.seterr(divide='ignore', invalid='ignore') #Sets how floating-point errors are handled.

arr = np.array([1.0, 0.0, 3.0])

print(np.reciprocal(arr)) #Returns the reciprocal of the argument, element-wise.