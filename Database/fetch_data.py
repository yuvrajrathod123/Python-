
import pymysql

def CreatConn():
    return pymysql.connect(host="localhost",database="lernvern",user="root",password="Yuvraj@5587",port=3306)

def showAllData():
    conn = CreatConn()
    cursor = conn.cursor()
    query = "select * from student"
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        print(i)

showAllData()

