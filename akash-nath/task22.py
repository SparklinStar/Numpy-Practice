#Task: Numpy compare with nonzero count
import numpy as np

#I didn't actually understand what to do in this task, so I'm gonna count non zero elements in an array

arr = np.array([[1, 0, 3],
                [0, 5, 0],
                [7, 0, 9]])

count = np.count_nonzero(arr) #Counts non zero elements from "arr" array

print(count)