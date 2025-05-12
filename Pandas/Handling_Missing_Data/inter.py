import pandas as pd

data={
    "Name": ["John", "Sam", "Peter", "Linda", "Mike", "Sara", "Tom", "Emma"],
    "age": [28, None, 35, 32, 50, 60, 45, 29],
    "salary": [50000, None, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score": [85,None, 72, 92, 88 ,95, 80, 89],   
}

df = pd.DataFrame(data)
print(df)

df.interpolate(method='linear',axis=0, inplace=True)
print(df)