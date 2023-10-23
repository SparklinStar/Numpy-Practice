import numpy as np


arr = np.array([1, 2, 3, 4, 5])
a = arr > 2
b = arr < 5
combined_condition = a & b

# Apply a custom process to matching elements
r = np.where(combined_condition, arr ** 2, arr)

print(r)
#end of task34
