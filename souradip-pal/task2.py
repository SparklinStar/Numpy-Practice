# Import the numpy library and give it the alias 'np'
import numpy as np

# 2. Check whether the array is empty

# Create two numpy arrays, 'a' (empty) and 'b' (non-empty).
a = np.array([])
b = np.array([1, 2])

# Define a function to check if a given array is empty or not.
def check_empty(a):
    # Check if the size of the array is 0, which indicates it's empty.
    if a.size == 0:
        print(a, ' : Empty')
    else:
        # If the array is not empty, print 'Non Empty'.
        print(a, ' : Non Empty')

# Call the function to check 'a' (empty array).
check_empty(a)

# Call the function to check 'b' (non-empty array).
check_empty(b)
