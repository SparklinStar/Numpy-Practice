#Task: Numpy inverse
import numpy as np

#Numpy inverse determines the inverse of a given square matrix. If given matrix A is non singular (|A|!=0) then it calculates the inverse of A [A^(-1)] so that A*A^(-1) = I. If singular matrix is given, "numpy.linalg.LinAlgError: Singular matrix" this error message appears.

arr = np.array([[1, 2, 9],
                [4, 5, 6],
                [7, 10, 9]])

arr_inv = np.linalg.inv(arr)

print(arr)
print(arr_inv) #Inverse matrix of matrix arr.