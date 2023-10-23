#Task: Compare Numpy datetime

import numpy as np

dt1 = np.datetime64('2023-10-15T12:30:00')
dt2 = np.datetime64('2023-10-15T14:45:00')

# Compare the datetime objects
print(dt1 < dt2)
print(dt1 <= dt2)
print(dt1 > dt2)
print(dt1 >= dt2)
print(dt1 == dt2)
print(dt1 != dt2)
