# write connection using snowflake python connector 
import snowflake.connector

# write a function to return the snowflake python connector to my database 
def get_connection():
    return snowflake.connector.connect (
        account='qa49151.us-central1.gcp',
        user='vbirbili',
        password='Viliana@2025',
        database='mydatabase',
        schema='public'
    )

