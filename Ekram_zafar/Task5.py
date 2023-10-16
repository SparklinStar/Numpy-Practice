# Import the numpy library and give it the alias 'np'
import numpy as np

# 5. Arrange numpy between numbers with intervals

# Create a numpy array 'c' using np.arange() that generates numbers starting from 12 up to (but not including) 30,
# with an interval of 3 between each number.
c = np.arange(12, 30, 3)

# Print the content of array 'c', which contains the numbers generated with a specified interval.
print(c)

# Print the shape (dimensions) of array 'c'.
print(c, '.shape : ', c.shape)
