import pandas as pd

# df = pd.read_json("sample_Data.json")  
 
data ={
    "Name": ["John", "Anna", "Peter", "Linda"],
    "age": [28, 24, 35, 32],
    "city": ["New York", "Paris", "Berlin", "London"]   
}

df = pd.DataFrame(data)

print('Displaying the info of data set :')
print(df.info())