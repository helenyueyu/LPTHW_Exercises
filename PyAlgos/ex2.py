import pandas as pd
import numpy as np

df = pd.DataFrame({
  'A': [0, 0, 1, None], 
  'B': [1, 2, 3, 4],
  'C': [np.NaN, 3, 4, 1]
  }, dtype=int)

print(df)

values = pd.Series(df.mean(), dtype=int)
print(values)

df2 = df.fillna(values)
print(df2)

