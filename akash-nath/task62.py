#Task: Seed for random

import numpy as np

#np.random.seed() is used to ensure reproducibility in code. By using this we can generate the same random numbers in the same order everytime I run the program

np.random.seed(0)
arr = np.random.randint(1, 11, size=(5, 5))

print(arr)