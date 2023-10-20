#Task: Get specific element

import numpy as np

arr = np.arange(1, 26).reshape(5, 5) #Creating a 5x5 matrix to get the element at 2nd row and 4th column

element = arr[1, 3] #This gets the element at 2nd row and 4th column

print(arr)
print(element)