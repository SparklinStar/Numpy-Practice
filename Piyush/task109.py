import numpy as np

# Create two sample arrays
array1 = np.array([[1, 2, 3]])
array2 = np.array([[4, 5, 6]])

# Append array2 to array1 along axis 0
appended_array = np.append(array1, array2, axis=0)

print("Array 1:")
print(array1)
print("Array 2:")
print(array2)
print("\nAppended along axis 0:")
print(appended_array)
