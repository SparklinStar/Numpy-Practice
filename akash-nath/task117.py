#Task: Resize a list with rounds

import numpy as np

original_list = [1.234567, 2.345678, 3.456789, 4.567890]
decimal_places = 2  # Set the number of decimal places to 2

rounded_list = [round(x, decimal_places) for x in original_list]

print(rounded_list)
