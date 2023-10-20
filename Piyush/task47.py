import numpy as np
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
array[0], array[9] = array[9], array[0]
print(array)
#end of task47
