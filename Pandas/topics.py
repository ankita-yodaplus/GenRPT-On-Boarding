"""
1 - how big is your daraset
2 - what are the names of columns

shape and columns
"""
import pandas as pd

data={
    "Name": ["John", "Anna", "Peter", "Linda", "Mike", "Sara", "Tom", "Emma"],
    "age": [28, 24, 35, 32, 50, 60, 45, 29],
    "salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85,90, 72, 92, 88 ,95, 80, 89],   
}

df =pd.DataFrame(data)
print(df)
print(f"Shape:{df.shape}")
print(f"Column Names:{df.columns}")

"""
(10000, 20)
(5, 4)
"""