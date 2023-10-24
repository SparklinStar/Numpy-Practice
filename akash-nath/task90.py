#Task: Boolean Numpy Array

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

#Creating a boolean array can be done in two methods

#Method - 1
print(arr > 5) #Returns a boolean array with True for elements greater than 5

#Method - 2
print(np.greater(arr,5)) #Returns a boolean array with True for elements greater than 5
