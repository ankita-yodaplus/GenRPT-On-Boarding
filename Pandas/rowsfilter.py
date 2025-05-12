import pandas as pd

data={
    "Name": ["John", "Anna", "Peter", "Linda", "Mike", "Sara", "Tom", "Emma"],
    "age": [28, 24, 35, 32, 50, 60, 45, 29],
    "salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score": [85,90, 72, 92, 88 ,95, 80, 89],   
}

df = pd.DataFrame(data)

high_salary = df[df["salary"] >50000]
print("High Salary Employees:")
print(high_salary)

# filtering rows age >50k and age >30

filtered_df = df[(df["salary"] > 50000) & (df["age"] > 30 )]
print("\nFiltered DataFrame (Salary > 50k and Age > 30):")  
print(filtered_df)

# using or Condition age >35  or performance score >90
filterd_or = df[(df["age"] > 35) | (df["Performance_Score"] > 90)]
print("\nFiltered DataFrame (Age > 35 or Performance Score > 90):")
print(filterd_or)