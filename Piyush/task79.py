import numpy as np
dates = np.array(['2023-10-26', '2023-10-27', '2023-10-28'], dtype='datetime64')
next_day = dates + np.timedelta64(1, 'D')
print(next_day)
#end of task 79
