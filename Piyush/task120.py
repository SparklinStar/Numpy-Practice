import numpy as np

start = 0.1
stop = 0.5
step = 0.1
arr = np.arange(start, stop, step)

value_to_compare = 0.2
print(np.isclose(arr, value_to_compare))
#end of task120
