import os
import pandas as pd
import snowflake.connector as sf
import db_info as db
from snowflake.connector.pandas_tools import write_pandas
import db_info
import datetime
file_path = r'C:\Users\Arun Raja\OneDrive\Documents\Grocessary\Vegetable_Purchase'
file_name = 'vegetable_purchase_tracker.csv'

purchase_df = pd.read_csv(filepath_or_buffer=os.path.join(file_path,file_name),sep=',')
purchase_df['PURCHASE_DT'] = pd.to_datetime(arg=purchase_df['PURCHASE_DT'],dayfirst= True ).dt.date
#print(purchase_df.columns)
#print(purchase_df.dtypes)
print(purchase_df.shape)
write_pandas(conn=db_info.connection,df = purchase_df,table_name= db_info.table_name,database= db_info.db_name,schema=db_info.schema_name)
print('Data Loaded Successfuly')

