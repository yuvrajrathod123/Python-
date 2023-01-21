
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

# showAllData()

# update data into database

def UpdateData(name,email,city,sid):
    conn = CreatConn()
    cursor = conn.cursor()
    args = (name,email,city,sid)
    query = "update student set name=%s,email=%s,city=%s where sid=%s"
    cursor.execute(query,args)
    conn.commit()
    print("data updated")

showAllData()  #show database before updating

sid = int(input("Enter your id:"))
n = input("Enter your name:")
e = input("Enter your email:")
c = input("Enter your city")

UpdateData(n,e,c,sid)   # for updteing

showAllData() # for showing updated data

# delete data fro, databse

def  DeleteData(sid):
    conn = CreatConn()
    cursor = conn.cursor()
    args = (sid)
    query = "delete from student where sid=%s"
    cursor.execute(query,args)
    conn.commit()
    print("data deleted")
    conn.close()

showAllData()

sid = int(input("enter your id"))

DeleteData(sid)
