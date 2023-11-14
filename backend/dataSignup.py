import psycopg2
import s

def addClient(userName, password, email):
    conn = psycopg2.connect(host=s.host, dbname=s.dbname, user=s.user, password=s.password, port=s.port)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute('SELECT * FROM login')
    rows = cur.fetchall()
    num = 0
    for row in rows:
        temp = row[0]
        temp = int(temp[3:])
        if num < temp:
            num = temp + 1
    num = str(num+1)
    while len(num) < 3:
        num = '0' + num
    id = 'CLI' + num
    print(id)
    cur.execute(f"INSERT INTO login (id,username,password,email) VALUES ('{id}', '{userName}', '{password}','{email}')")
    cur.close()
    conn.close()