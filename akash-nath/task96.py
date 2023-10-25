#Task: If condition and sum on Numpy colum

import numpy as np

data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])


condition = data[:, 1] > 3 #Define the condition to select elements greater than 3 in the second column

selected_elements = data[condition, 1]

column_sum = np.sum(selected_elements) # Calculate the sum of the selected elements

print(column_sum)