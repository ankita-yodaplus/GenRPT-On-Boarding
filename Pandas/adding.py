import pandas as pd

data={
    "Name": ["John", "Anna", "Peter", "Linda", "Mike", "Sara", "Tom", "Emma"],
    "age": [28, 24, 35, 32, 50, 60, 45, 29],
    "salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score": [85,90, 72, 92, 88 ,95, 80, 89],   
}

df = pd.DataFrame(data)
print(df)

#adding column
# Square brackets df["Column Name"] = some_Data

df["Bonus"] = df["salary"] * 0.1
print(df)

#using insert() method
#df.insert(loc, "Column_Name", some_data)

df.insert(0,"Emp_Id",[10,20,30,40,50,60,70,80])
print(df)