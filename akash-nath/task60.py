#Task: Shuffle

import numpy as np

arr = np.array([[10, 7, 4],
                [3, 2, 1],
                [6, 8, 2]])

print(arr)
np.random.shuffle(arr) #Shuffles the rows of the array

print(arr)