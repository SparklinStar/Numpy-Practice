#Task: Numpy Where

import numpy as np

#We use np.where() to perform specific logic for each elements of an array. The syntax is kind of like this: np.where(condition, x, y). It can be said that this is an if-else codition for arrays. If the condition "condition" returns true, x is executed, else y is executed.

arr = np.arange(1, 50, 3)

result = np.where(arr > 25, 10, 20) #This will return an array containing 10 if the number at that position is greater than 25, and 20 if that number is not greater than 25

print(result)