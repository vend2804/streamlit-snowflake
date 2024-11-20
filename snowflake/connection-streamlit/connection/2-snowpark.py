#write the code from 1-connector.py using snowpark connector 
import os
from snowflake.snowpark import Session

session = Session.builder.configs(
   account='qa49151.us-central1.gcp',
        user='vbirbili',
        password='Viliana@2025',
        database='mydatabase',
        schema='public'
).create()

df = session.table("employees").toPandas()
print(df)

session.close()
