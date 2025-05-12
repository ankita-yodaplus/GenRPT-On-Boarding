import pandas as pd

#customer dataframe
df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown'],
})

order_df = pd.DataFrame({
    'CustomerID': [1, 2, 4],
    'OrderAmount': [250, 150, 300]
})

#merge
# df_merged = pd.merge(df_customers, order_df, on='CustomerID', how='inner')
# print("Inner Join:")
# print(df_merged)

# df_merged = pd.merge(df_customers, order_df, on='CustomerID', how='outer')
# print("Outer join:")
# print(df_merged)

# df_merged = pd.merge(df_customers, order_df, on='CustomerID', how='left')
# print("Left join:")
# print(df_merged)

# df_merged = pd.merge(df_customers, order_df, on='CustomerID', how='right')
# print("right join:")
# print(df_merged)

df_merged = pd.merge(df_customers, order_df, how='cross')
print("Cross join:")
print(df_merged)

