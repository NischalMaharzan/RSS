import psycopg2
from psycopg2.extras import RealDictCursor 
# //This allows to get the column name of the table
import time
from config import settings

def database_connection():
    while True:
        try: 
            conn = psycopg2.connect(
                host=settings.database_hostname,
                database=settings.database_name,
                user=settings.database_username,
                password=settings.database_password,
                cursor_factory=RealDictCursor)
            print("DATABASE CONNECTION SUCCESSFUL>>>")
            break
        except Exception as error:
            print ("DATABASE CONNECTION FAILED!!!")
            print (error)
            time.sleep(2)

    return conn
        
