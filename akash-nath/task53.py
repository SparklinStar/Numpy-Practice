#Task: Covariance matrix
import numpy as np

arr = np.array([[10, 7, 4],
                [3, 2, 1],
                [6, 8, 2]])

print(arr)
print(np.cov(arr)) #Prints the covariance matrix of the array