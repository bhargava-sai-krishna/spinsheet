import psycopg2
import pandas as pd
from io import BytesIO

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="sbskln2412S", port=5432)
cursor = conn.cursor()

cursor.execute("SELECT FileName, FileType, FileData FROM Files WHERE FileID = 2")
record = cursor.fetchone()

file_name, file_type, file_data = record

# Convert binary data to a DataFrame
df = pd.read_excel(BytesIO(file_data))

# Now you can work with the DataFrame (df) as needed
print(df)

cursor.close()
conn.close()
