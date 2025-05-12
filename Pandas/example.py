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

print("Names (Single column return series)")
# print(df["Name"])
name =  df["Name"]
print(name)

#selecting multiple columns
# subset =df[["Name", "age"]]
# print(subset) 
subset = df[["Name","salary"]]
print('\n Subset with Name and Salary')
print(subset)