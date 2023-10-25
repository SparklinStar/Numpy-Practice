import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

flipped_arr = np.flipud(arr).copy()

print("Original array:\n", arr)
print("Flipped array:\n", flipped_arr)
