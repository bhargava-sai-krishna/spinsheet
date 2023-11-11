from flask import Flask,request,Response
from flask_cors import CORS
import psycopg2
import s

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

@app.route('/sendTempPass',methods=['GET','POST'])
def tempPasser():
    dataJson=request.get_json()
    userId=dataJson['userId']
    conn = psycopg2.connect(host=s.host, dbname=s.dbname, user=s.user, password=s.password, port=s.port)
    cur = conn.cursor()

if __name__=="__main__":
    app.run(debug=True)