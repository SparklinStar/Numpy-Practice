

#Dataframe to Numpy
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Extract the column names and data
column_names = df.columns
data = df.values

# Convert the data to a NumPy array
numpy_array = np.array(data)
#end of task14
