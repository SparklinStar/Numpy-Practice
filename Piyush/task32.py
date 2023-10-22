import numpy as np

arr = np.array([1, 2, 3, 4, 5])
a = arr >3
b = arr <5

result = np.where(a & b, arr, 0)

print(result)
#end of task32
