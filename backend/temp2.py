import psycopg2
conn = psycopg2.connect(
    host="localhost",
    dbname="spinsheet",
    user="postgres",
    password="sbskln2412S",
    port=5432
)
cursor = conn.cursor()

with open('C:/Users/bhargava/Documents/react/spinsheet/backend/airquality.xlsx', 'rb') as file:
    file_data = file.read()

cursor.execute("INSERT INTO files (id, FileName, FileType, FileData) VALUES (%s, %s, %s, %s)",
               ('CLI001', 'airquality.xlsx', 'xlsx', psycopg2.Binary(file_data)))

with open('C:/Users/bhargava/Documents/react/spinsheet/backend/diabetes.csv', 'rb') as file:
    file_data = file.read()

cursor.execute("INSERT INTO files (id, FileName, FileType, FileData) VALUES (%s, %s, %s, %s)",
               ('CLI001', 'diabetes.csv', 'csv', psycopg2.Binary(file_data)))

with open('C:/Users/bhargava/Documents/react/spinsheet/backend/WineQT.csv', 'rb') as file:
    file_data = file.read()

cursor.execute("INSERT INTO files (id, FileName, FileType, FileData) VALUES (%s, %s, %s, %s)",
               ('CLI001', 'WineQT.csv', 'csv', psycopg2.Binary(file_data)))

conn.commit()
cursor.close()
conn.close()
