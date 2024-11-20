import os
import pandas

from snowflake.snowpark import Session

# Write me a connection to Snowflake using snowpark 
def get_connection():
    return Session.builder.configs({
        "account": 'qa49151.us-central1.gcp',
        "user": 'vbirbili',
        "password": 'Viliana@2025',
        "database": 'mydatabase',
        "schema": 'public'
        }).create()






