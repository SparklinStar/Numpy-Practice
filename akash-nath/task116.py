#Task: Convert List of List String to Numpy Array

import numpy as np

list_of_list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

arr = np.array(list_of_list, dtype = np.int32)

print(arr)