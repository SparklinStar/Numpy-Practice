#Task: Flip a numpy array by using flip (both horizontally and vertically)
import numpy as np

#In this task I'm gonna first flip the array vertically, and then I'm gonna flip that flipped array horizontally

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

verticalArr = np.flipud(arr)

horizontalArr = np.fliplr(verticalArr)

print(arr)
print(verticalArr)
print(horizontalArr)