import psycopg2
import s
import pandas as pd
import io
import json

def fun(userId, table_data):
    df = pd.DataFrame([table_data])
    print(df)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    # Convert JSON to bytes
    json_bytes = json.dumps(json_data).encode('utf-8')
    
    # Connect to the database
    conn = psycopg2.connect(host=s.host, dbname=s.dbname, user=s.user, password=s.password, port=s.port)
    conn.autocommit = True
    cur = conn.cursor()

    # Update the filedata in the database
    cur.execute("UPDATE files SET filedata = %s WHERE id = %s", (psycopg2.Binary(json_bytes), userId))

    # Close the database connection
    cur.close()
    conn.close()
