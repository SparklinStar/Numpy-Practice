#Task: Using Flipud
import numpy as np

#Flipud flips the array virtically. So the first row becomes the last one, and the last one becomes the first one

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

flipped_arr = np.flipud(arr)
"""
The output should be like this
[[7, 8, 9],
[4, 5, 6],
[1, 2, 3]]
"""

print(arr)
print(flipped_arr)