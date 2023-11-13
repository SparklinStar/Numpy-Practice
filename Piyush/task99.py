import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6])

# Define a condition (e.g., values greater than 3)
condition = (arr > 3)

# Replace values that meet the condition with a new value (e.g., 0)
arr[condition] = 0

print("Modified Array:")
print(arr)
