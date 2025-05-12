#sorting data 1 column sort_values()

# df.sort_values(by = 'Column Name')
import pandas as pd

data ={
    "Name":['Arun', 'Varun', 'Karun'],
    "Age":[28,34,22],
    "Salary":[100000,20000,3000],
}

df = pd.DataFrame(data)
df.sort_values(by=["Age", "Salary"], ascending=[True,False], inplace=True)
print("Sorting by Age in Descending Order:")
print(df)