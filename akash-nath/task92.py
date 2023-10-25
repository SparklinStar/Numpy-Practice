#Task: Replace values with specific condition

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

#Replacing all odd numbers with -1
arr[arr%2==1] = 0

print(arr)