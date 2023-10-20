#Task: Process with where
import numpy as np

#We can process different logics using np.where()

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

result1 = np.where((arr>5)|(arr>7), 0, 1)
result2 = np.where((arr>5)&(arr>7), 0, 1)

print(result1)
print(result2)