# head() tail()
# head () -5
# tail (n) -5 

import pandas as pd

df = pd.read_json("sample_Data.json")

print('Display First 10 rows:')
print(df.head(10))

print('Display Last 10 rows:')
print(df.tail(10))