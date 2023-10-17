import numpy as np
# Creating an empty array
array = np.empty((3, 3))  
# Check if the array is empty
is_empty = np.all(array == 0)

if is_empty:
    print("The array is empty.")
else:
    print("The array is not empty.")
    #the task2 completion
