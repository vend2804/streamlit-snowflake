import os
import pandas
import snowflake.connector

conn = snowflake.connector.connect(
    account='qa49151.us-central1.gcp',
    user='vbirbili',
    password='Viliana@2025',
    database='mydatabase',
    schema='public'

)

cur = conn.cursor()
cur.execute("select * from mydatabase.public.employees")
#one_row = cur.fetchone()
#print(one_row[0])   
df = cur.fetch_pandas_all()
print(df)

#for row in cur:
 #   print(row)


cur.close()
conn.close()