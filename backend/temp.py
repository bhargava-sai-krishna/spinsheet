import psycopg2
import pandas as pd
from io import BytesIO

conn = psycopg2.connect(host="localhost", dbname="spinsheet", user="postgres", password="sbskln2412S", port=5432)
cursor = conn.cursor()

cursor.execute("SELECT filedata FROM files WHERE id='CLI001' AND filename='WineQT.csv'")
record = cursor.fetchone()

if record is not None:
    bytes_data = record[0]
    bytes_io = BytesIO(bytes_data)
    df = pd.read_csv(bytes_io)

    # Now you can work with the DataFrame 'df'
    print(df)
else:
    print("No record found.")

# Close the cursor and connection
cursor.close()
conn.close()
