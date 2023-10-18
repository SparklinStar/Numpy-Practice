# 14. Dataframe to Numpy

# Import the Pandas library
import pandas as pd

# Create a DataFrame named 'df' with two columns 'a1' and 'a2', and custom indices 'X', 'Y', and 'Z'
df = pd.DataFrame({'a1': [1, 2, 3], 'a2': [4, 5, 6]}, index=['X', 'Y', 'Z'])

# Print the original DataFrame
print('Dataframe:')
print(df)

# Convert the DataFrame to a NumPy array and store it in 'x'
x = df.to_numpy()

# Print the DataFrame converted to a NumPy array
print('\nDataframe to Numpy:')
print(x)

# Extract the index of the DataFrame and convert it to a NumPy array 'y'
y = df.index.to_numpy()

# Print the DataFrame's index converted to a NumPy array
print('\nDataframe Indices to Numpy:')
print(y)

# Extract the 'a1' column as a NumPy array 'z'
z = df['a1'].to_numpy()

# Print the 'a1' column as a NumPy array
print('\nDataframe Series to Numpy:')
print(z)
