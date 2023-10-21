#Task: Count the number of occurrences

import numpy as np

arr = np.array([[10, 7, 4],
                [3, 2, 1],
                [6, 8, 2]])

print(arr)
print(np.count_nonzero(arr == 2)) #Prints the number of occurrences of 2 in the array