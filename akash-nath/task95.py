#Task: If condition on Numpy array on the fly

import numpy as np

data = np.array([1, 2, 3, 4, 5])

condition = (data > 3)  # Create a boolean mask for elements greater than 3
result = data[condition]  # Select elements that meet the condition

print(result)