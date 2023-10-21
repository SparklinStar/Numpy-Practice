#Task: Calculate 90th percentile of an axis

import numpy as np

arr = np.array([[10, 7, 4],
                [3, 2, 1],
                [6, 8, 2]])

print(arr)
print(np.percentile(arr, 90, axis=0))