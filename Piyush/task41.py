import numpy as np
import datetime
today = np.datetime64(datetime.date.today())
delta = np.timedelta64(7, 'D')  # 7 days
future_date = today + delta
past_date = today - delta
print("Today's date:", today)
print("Date 7 days in the future:", future_date)
print("Date 7 days in the past:", past_date)
#end of task 41
