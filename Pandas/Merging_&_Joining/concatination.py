
# vertical
import pandas as pd

df_Region1 = pd.DataFrame({
    "CustomerID":[1,2],
    "Name":["John", "Jane"],
})  

df_Region2 = pd.DataFrame({
    "CustomerID":[3,4],
    "Name":["Sneh", "Jasmin"],
}) 

# df_concat = pd.concat([df_Region1, df_Region2], ignore_index=True)
# print("Vertical Concatenation:")
# print(df_concat)

df_concat = pd.concat([df_Region1, df_Region2],axis=1, ignore_index=True)
print("Horizontal Concatenation:")
print(df_concat)