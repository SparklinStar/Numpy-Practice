import numpy as np
date = np.datetime64('2023-10-26')
date2 = np.datetime64('2023-10-27')
is_equal = date == date2
is_not_equal = date != date2
is_less_than = date < date2
is_greater_than = date > date2
is_less_than_or_equal = date <= date2
is_greater_than_or_equal = date >= date2
print("Is Equal:", is_equal)
print("Is Not Equal:", is_not_equal)
print("Is Less Than:", is_less_than)
print("Is Greater Than:", is_greater_than)
print("Is Less Than or Equal:", is_less_than_or_equal)
print("Is Greater Than or Equal:", is_greater_than_or_equal)
#end of task81
