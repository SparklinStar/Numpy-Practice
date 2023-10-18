#Task: Numpy where with multiple conditions

import numpy as np

arr = np.arange(1, 10)

condition1 = arr>6
condition2 = arr>3

#We can use and (&), or (|), not(~) operator to work with multiple conditions

#And(&) operator
result1 = np.where(condition1 & condition1, 1, 0)
print(result1)

#Or(|) operator
result2 = np.where(condition1 | condition2, 1, 0)
print(result2)

#Not(~) operator
result3 = np.where(~condition1, 1, 0)
print(result3)