#Task: Roll elements

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(arr)
# Roll the elements to the left by 2 positions
rolled_arr = np.roll(arr, shift=2)
print("Rolled Array:\n", rolled_arr)