import pandas as pd

#read data from csv file into dataframe
# df =pd.read_csv("sales_data_sample.csv", encoding="latin1")
# df =pd.read_excel("SampleSuperstore.xlsx") 
df = pd.read_json("sample_Data.json")

print(df)