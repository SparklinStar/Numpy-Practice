import numpy as np
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a = np.percentile(m, 90, axis=1)
print("90th percentile along each row:", a)
#end of task56
