#Task: Get the nth column of an array
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

n = 2

nth_column = arr[:,n] #":" represents all columns, and then the "n" tells the program that we want only the n_th column out of all columns in the array

print(nth_column)