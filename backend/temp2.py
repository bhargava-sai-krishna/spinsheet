import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="sbskln2412S", port=5432)
cursor = conn.cursor()

with open('C:/Users/bhargava/Documents/react/spinsheet/backend/airquality.xlsx', 'rb') as file:
    file_data = file.read()

cursor.execute("INSERT INTO Files (FileName, FileType, FileData) VALUES (%s, %s, %s)",
               ('your_file.xlsx', 'xlsx', psycopg2.Binary(file_data)))

conn.commit()
cursor.close()
conn.close()
