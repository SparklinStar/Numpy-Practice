#Task: Random int array and sorting

import numpy as np

arr = np.random.randint(1, 20, 10)

sorted_arr = np.sort(arr)

#Sorting in descending order (descending: life description fr :))

decending_arr = np.sort(arr)[::-1]

print("Generated array", arr)
print("Sorted array", sorted_arr)
print("Descending order sorted array", decending_arr)
