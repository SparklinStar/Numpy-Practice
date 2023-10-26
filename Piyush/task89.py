import numpy as np

# Create two NumPy arrays
array1 = np.array([[10, 20], [30, 40]])
array2 = np.array([[5, 6]])

# Concatenate along rows (vertically)
concatenated_array = np.concatenate((array1, array2), axis=0)

print(concatenated_array)
#end of task89
