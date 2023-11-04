import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
raveled_array = arr.ravel()
raveled_array[0] = 999

print("Original Array:")
print(arr)

print("Raveled Array:")
print(raveled_array)
flattened_array = arr.flatten()
flattened_array[0] = 999

print("Original Array:")
print(arr)

print("Flattened Array:")
print(flattened_array)
#end of task88
