import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Reshape the array with C-order (row-major order)
reshaped_c_order = arr.reshape((3, 2), order='C')
print("Reshaped with C-order:")
print(reshaped_c_order)

# Reshape the array with F-order (column-major order)
reshaped_f_order = arr.reshape((3, 2), order='F')
print("\nReshaped with F-order:")
print(reshaped_f_order)
#end of task114
