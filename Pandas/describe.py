# step1 - sample data frame
import pandas as pd

data={
    "Name": ["John", "Anna", "Peter", "Linda", "Mike", "Sara", "Tom", "Emma"],
    "age": [28, 24, 35, 32, 50, 60, 45, 29],
    "salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85,90, 72, 92, 88 ,95, 80, 89],   
}

df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)
print("\n")
print("Descriptive Statistics:")
print(df.describe())