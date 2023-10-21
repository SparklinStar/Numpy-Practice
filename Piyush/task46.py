import numpy as np
arr = np.array([1, 5, 8, 12, 18, 25, 30])
value = 15
abs_diff = np.abs(arr - value)
nearest_index = np.argmin(abs_diff)
nearest_element = arr[nearest_index]
print("Nearest Element:", nearest_element)
print("Index of Nearest Element:", nearest_index)
#end of task46
