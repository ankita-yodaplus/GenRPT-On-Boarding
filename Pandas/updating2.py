import pandas as pd

data={
    "Name": ["John", "Anna", "Peter", "Linda", "Mike", "Sara", "Tom", "Emma"],
    "age": [28, 24, 35, 32, 50, 60, 45, 29],
    "salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score": [85,90, 72, 92, 88 ,95, 80, 89],   
}

df = pd.DataFrame(data)
print(df)

# increasing salary by 5%
df['salary'] = df['salary'] * 1.05
print(df)
