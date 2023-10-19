#Task: Numpy where with multiple conditions - apply only on matching conditions

import numpy as np

arr = np.array([1, 7, 12, 3, 8, 15, 4, 9, 6, 10])

condition1 = arr > 5
condition2 = arr < 10
condition3 = arr % 2 == 0

combined_condition1 = condition1 & condition2 & condition3
combined_condition2 = condition1 | condition2 | condition3

result1 = np.where(combined_condition1)
result2 = np.where(combined_condition2)

selected_elements1 = arr[result1]
selected_elements2 = arr[result2]

print(selected_elements1)
print(selected_elements2)
