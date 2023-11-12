from flask import Flask,request,Response
from flask_cors import CORS
import psycopg2
import s
import json
import pandas as pd
from io import BytesIO

app=Flask(__name__)
CORS(app)

@app.route('/success')
def success():
    return 'success'

@app.route('/signin', methods=['GET','POST'])
def signin():
    data=request.get_json()
    userId = data['userId']
    password = data['password']
    conn = psycopg2.connect(host=s.host, dbname=s.dbname, user=s.user, password=s.password, port=s.port)
    cur = conn.cursor()
    cur.execute("select * from login")
    rows= cur.fetchall()
    flag="False"
    name=""
    for row in rows:
        if((userId==row[0] and password==row[2])or(userId==row[3] and password==row[2])):
            flag=row[0]
            name=row[1]
    cur.close()
    conn.close()
    data={
        "flag" : flag,
        "name" : name,
    }
    return data

@app.route('/getFiles',methods=['GET','POST'])
def tempPasser():
    data=request.get_json()
    userId = data['userId']
    conn = psycopg2.connect(host=s.host, dbname=s.dbname, user=s.user, password=s.password, port=s.port)
    cur = conn.cursor()
    cur.execute(f"select id,filename,filetype from files where id='{userId}'")
    rows = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]
    dict_rows = [dict(zip(column_names, row)) for row in rows]
    dict_rows = json.dumps(dict_rows)
    return dict_rows

@app.route('/getExcel',methods=['GET','POST'])
def GetExcel():
    data=request.get_json()
    userId = data['userId']
    filename=data['filename']
    conn = psycopg2.connect(host="localhost", dbname="spinsheet", user="postgres", password="sbskln2412S", port=5432)
    cursor = conn.cursor()
    cursor.execute(f"select filedata from files where id='{userId}' and filename='{filename}'")
    record = cursor.fetchone()
    bytes_data = record[0]
    bytes_io = BytesIO(bytes_data)
    if filename[-1]=='x':
        df = pd.read_excel(bytes_io)
    else:
        df=pd.read_csv(bytes_io)
    json_data=df.to_json(orient='records')
    return json_data

if __name__=="__main__":
    app.run(debug=True)