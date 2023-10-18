#Task: Numpy view
import numpy as np

#Numpy view is the same data in different objects. If we change any of those object's value, the value of other one changes as well.

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

viewedArr = arr.view()

print(arr)
print(viewedArr)

viewedArr[0][2] = 10 #This should change the value from the "arr" array as well.

print(arr)
print(viewedArr)