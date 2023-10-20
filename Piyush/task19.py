import numpy as np

# Create a NumPy array
a = np.array([1, 2, 3, 4, 9])

# Create a view of the original array
a_view = a.view()

# Change an element in the view
a_view[0] = 10
print("Original array:", a)

print("View:", a_view)
#end of task19
