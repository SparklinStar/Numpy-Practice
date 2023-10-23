#Task: Pretty print - suppress the scientific notation

import numpy as np

#np.set_printoptions() sets printing options

arr = np.array([1.6e-10, 1.6, 1200, .235])

print(arr)

np.set_printoptions(suppress=True)

print(arr)