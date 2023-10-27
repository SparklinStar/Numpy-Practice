#Task: Where with multiple condition

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

condition = (arr % 2 == 0) & (arr > 4)
result = np.where(condition, arr, 0)

print(result)