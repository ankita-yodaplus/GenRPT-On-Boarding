import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:root@localhost:5432/satutorialdatabase')

df= pd.read_sql('SELECT * FROM people', con=engine)
print(df)

# new_data = pd.DataFrame({'name':['Florian','Jack'], 'age' :[25,80]})
# new_data.to_sql('people', con=engine, if_exists='append', index=False)