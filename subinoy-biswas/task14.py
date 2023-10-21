import pandas as pd
import numpy as np

meowdf = pd.DataFrame({'A':[1,2,3,4],'B':[1,3,5,7]})
meowdf = meowdf.rename_axis("S")
print(meowdf)
meownp = meowdf.to_numpy()
print(meownp)