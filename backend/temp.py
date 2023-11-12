import psycopg2
import pandas as pd
from io import BytesIO

conn = psycopg2.connect(host="localhost", dbname="spinsheet", user="postgres", password="sbskln2412S", port=5432)
cursor = conn.cursor()

cursor.execute("select filedata from files where id='CLI001' and filename='airquality.xlsx'")
record = cursor.fetchone()


# Extract the BytesIO object from the tuple
bytes_data = record[0]

# Use BytesIO to create a BytesIO object
bytes_io = BytesIO(bytes_data)

# Read the Excel file from BytesIO
df = pd.read_excel(bytes_io)

# Now you can work with the DataFrame 'df'
print(df)
