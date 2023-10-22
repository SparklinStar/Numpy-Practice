import numpy as np

a = np.array([1, 2, 3, 4, 5])
condition = a > 3

result = np.where(condition, a, 0)

print(result)
#end of task31
