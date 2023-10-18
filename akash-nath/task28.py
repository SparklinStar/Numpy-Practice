#Task: Convert numpy array to list

import numpy as np

#We can use tolist() function to make the numpy array a list

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

listArr = arr.tolist() #Converting "arr" array to python list

print(listArr)