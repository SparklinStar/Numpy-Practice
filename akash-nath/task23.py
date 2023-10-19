#Task: Flip a numpy array by using flipud
import numpy as np

#In this task we have to flip the array vertically, so that the first row becomes last row, and the last one becomes first row.

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

reversed_arr = np.flipud(arr)

print(arr)
print(reversed_arr)