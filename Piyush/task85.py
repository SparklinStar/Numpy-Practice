import pandas as pd
import numpy as np
numpy_array = np.array([(1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 35)])
column_names = ['ID', 'Name', 'Age']
df = pd.DataFrame.from_records(numpy_array, columns=column_names)
print(df)
#end of task85
