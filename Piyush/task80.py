import numpy as np
start_date = np.datetime64('2023-10-26')
end_date = np.datetime64('2023-11-05')
step = np.timedelta64(1, 'D')
datetime_range = np.arange(start_date, end_date, step)
print(datetime_range)
#end of task 80
