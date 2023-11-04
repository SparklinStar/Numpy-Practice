#Task: Selecting specific columns

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

selected_columns = arr[:, [0, 2]] #Select the 1st and 3rd columns

print(selected_columns)


