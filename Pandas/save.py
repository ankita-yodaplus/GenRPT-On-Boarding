import pandas as pd

data ={
    "Name": ["John", "Anna", "Peter", "Linda"],
    "age": [28, 24, 35, 32],
    "city": ["New York", "Paris", "Berlin", "London"]   

}

df = pd.DataFrame(data)
print(df)

# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)