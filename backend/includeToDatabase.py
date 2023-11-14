import psycopg2
import s
import pandas as pd
import io

def fun(userId, df, ftype, name):
    # Convert DataFrame to CSV format in-memory
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_data = csv_buffer.getvalue()

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(host=s.host, dbname=s.dbname, user=s.user, password=s.password, port=s.port)
    conn.autocommit = True
    cur = conn.cursor()

    try:
        # Insert the data into the database
        cur.execute(f"INSERT INTO files(id, filename, filetype, filedata) VALUES (%s, %s, %s, %s)", (userId, name, ftype, csv_data))
    except Exception as e:
        print(f"Error inserting data into the database: {e}")
    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()
