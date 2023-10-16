# Import the numpy library and give it the alias 'np'
import numpy as np

# 3. Check elements count

# Create two numpy arrays, one empty and one with elements
c = np.array([])
d = np.array([1, 2])

# Define a function named get_elements that takes one argument 'c_array'.
def get_elements(c_array):
    # Return the number of elements in the array
  
    return c_array.size
        
# Print the content of array 'c' and its elements count
print(c, ', elements_count : ', get_elements(c))

# Print the content of array 'd' and its elements count
print(d, ', elements_count : ', get_elements(d))
