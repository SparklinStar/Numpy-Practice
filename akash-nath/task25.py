#Task: Flip a numpy array by using fliplr
import numpy as np

#In this task we have to flip the array horizontally, so that the first column becomes last column, and the last one becomes first column.

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

reversed_arr = np.fliplr(arr)

print(arr)
print(reversed_arr)