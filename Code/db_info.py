# Vegetable Data

import os
import snowflake.connector as sf
from snowflake.connector.pandas_tools import write_pandas
import sf_setup_parm as parm

db_name = 'PURCHASE_DB'
schema_name = 'VEG_PURCHASE'
table_name = 'VEGETABLE_PURCHASE_TRAN_TBL'

connection = sf.connect(user = parm.user_name,password = parm.pwd,account = parm.account_id,role = parm.role,warehouse = parm.wh)
connection.cursor().execute(f'USE ROLE {parm.role}')
connection.cursor().execute(f'USE WAREHOUSE {parm.wh}')
connection.cursor().execute(f'USE DATABASE {db_name}')
connection.cursor().execute(f'USE SCHEMA {schema_name}')
connection.cursor().execute(f'TRUNCATE TABLE {db_name}.{schema_name}.{table_name}')




