import numpy as np

arr = np.array([10, 20, 30, 40, 50])
a = arr > 2
b = arr < 5

combined_condition = condition1 & condition2

result = np.where(combined_condition, arr, 0)

print(result)
#end of task33
