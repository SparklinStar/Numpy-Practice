#Taks: Apply Along Axis on Numpy Matrix
import numpy as np

matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

row_sums = np.sum(matrix, axis=0)
column_sums = np.sum(matrix, axis=1)

print(row_sums)
print(column_sums)

row_means = np.mean(matrix, axis=0)
column_means = np.mean(matrix, axis=1)

print(row_means)
print(column_means)