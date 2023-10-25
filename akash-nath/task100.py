#This is the 100th task of this numpy practice session. Learnt a lot of things in past 100 task. Looking forward to get more practice sessions like this

#Task: Numpy Roll

import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Roll the elements of the entire array to the left by 1 position
rolled_arr = np.roll(arr, shift=1)

print(rolled_arr)