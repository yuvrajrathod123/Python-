# import pymysql
from fetch_data import*

# def CreatConn():
#     return pymysql.connect(host="localhost",database="lernvern",user="root",password="Yuvraj@5587",port=3306)

def showAllDataById(sid):
    conn = CreatConn()
    cursor = conn.cursor()
    args = sid
    query = "select * from student where sid=%s"
    cursor.execute(query,args)
    result = cursor.fetchall()
    for i in result:
        print(i)

showAllData()

sid = int(input("enter your id:"))

showAllDataById(sid)

