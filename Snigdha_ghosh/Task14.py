import numpy as np

df = pd.DataFrame({'a1': [1, 2, 3], 'a2': [4, 5, 6]}, index=['X', 'Y', 'Z'])

print(df)
x = df.to_numpy()
print(x)
y = df.index.to_numpy()
print('Dataframe Indices to Numpy:')
print(y)
z = df['a1'].to_numpy()
print('\nDataframe Series to Numpy:')
print(z)
