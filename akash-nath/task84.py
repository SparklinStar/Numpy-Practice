#Task: Reverse 2D Array

import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

#Reversing an 2D array can be done in two methods

#Method - 1
print(arr[::-1]) #Reverse the array using slicing, reverses only rows

#Method - 2
print(np.flip(arr)) #Reverse the array using flip() function, reverses both rows and column