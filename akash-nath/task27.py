#Task: Flipping the numpy array using slices
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

flipped_arr = arr[:, ::-1] #We are selecting all columns with ":", and then flipping each of them using "::-1"

print(flipped_arr)
