import numpy as np

arr = np.array([1, 6, 7, 3, 11, 9, 2, 8, 5])

condition1 = arr > 5
condition2 = arr < 10

combined_condition = condition1 & condition2

result = arr[combined_condition]

print(result)
#end of task116
