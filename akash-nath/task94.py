#Task: Vectorize

import numpy as np

#Vectorize is a function that converts a function into a vectorized function
#A vectorized function is a function that can operate on vectors
#For example, if we have a function that adds two numbers, we can convert it to a vectorized function
#This vectorized function can now add two vectors
#This is useful when we want to apply a function to a numpy array

def my_function(x):
    return x * 2

vectorized_my_function = np.vectorize(my_function)
arr = np.array([1,2,3,4,5])
print(vectorized_my_function(arr))