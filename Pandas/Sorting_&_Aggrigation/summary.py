import pandas as pd
data ={
    "Name":['Arun', 'Varun', 'Karun', 'Ravi','Shyam'],
    "Age":[28, 35, 22, 35, 28],
    "Salary":[28000,34000, 60000, 22000, 16000],
}

df = pd.DataFrame(data)
avg_salary = df['Salary'].mean()
print("Average Salary:", avg_salary)
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)