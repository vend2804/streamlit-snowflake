import os
import snowflake.connector

conn = snowflake.connector.connect(
     account='qa49151.us-central1.gcp',
        user='vbirbili',
        password='Viliana@2025',
        database='mydatabase',
        schema='public'
)

# (1) fetching row by row
cur = conn.cursor()
cur.execute('select * from mydatabase.public.employees')
for row in cur: print(row)

# (2) getting the whole set
df = cur.fetch_pandas_all()
print(df)