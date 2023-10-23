#Task: Numpy array to Pandas Dataframe

import numpy as np
import pandas as pd

arr = np.array([[1, 2, 3], [4, 5, 6]])
df = pd.DataFrame(arr)

print(arr)
print(df)