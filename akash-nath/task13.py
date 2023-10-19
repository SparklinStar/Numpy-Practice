#Task: Dataframe to Numpy
import numpy as np
import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data) #Pandas Dataframe

numpy_array = df.values

print(numpy_array)