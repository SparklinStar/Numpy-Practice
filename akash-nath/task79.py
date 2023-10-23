#Task: Numpy to Dataframe by using from_records

import numpy as np
import pandas as pd

arr = np.array([('John', 25, 92.5), ('Lisa', 35, 75.5), ('Peter', 27, 88.5)])

df = pd.DataFrame.from_records(arr, columns=['Name', 'Age', 'Score'])

print(arr)
print(df)