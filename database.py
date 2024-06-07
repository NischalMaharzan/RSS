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
        

# conn = database_connection()    
# cur = conn.cursor()

# # Execute a command: this creates a new table
# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# # Pass data to fill a query placeholders and let Psycopg perform

# # the correct conversion (no more SQL injections!)
# cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))

# # Query the database and obtain data as Python objects
# cur.execute("SELECT * FROM test;")
# cur.fetchone()

# # Make the changes to the database persistent
# conn.commit()

# # Close communication with the database
# cur.close()
# conn.close()

