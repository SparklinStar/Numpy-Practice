#Task: Flip a numpy array by using flipud without sharing the memory
import numpy as np

#We have to flip an array in a manner so that 2 arrays are alocated in different positions in memory. We can flip it and use .copy() funtion to make sure they are not in same position in memory.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

flipped_arr = np.flipud(arr).copy()

print("Original array:\n", arr)
print("Flipped array:\n", flipped_arr)
