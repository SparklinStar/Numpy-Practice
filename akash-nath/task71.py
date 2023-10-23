#Task: Print with decimal format

import numpy as np

arr = np.array([1.23456, 2.34567, 3.45678])

# Format each element with 2 decimal places and then print the formatted array
formatted_arr = np.array2string(arr, precision=2, formatter={'float': lambda x: f'{x:.2f}'})

print(formatted_arr)
