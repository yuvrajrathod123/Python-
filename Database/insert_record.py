
# from yuvi import CreatConn
import pymysql

def CreatConn():
    return pymysql.connect(host="localhost",database="lernvern",user="root",password="Yuvraj@5587",port=3306)

def InsertData(name,email,city):
    conn = CreatConn()   #creating connnection
    cursor = conn.cursor()
    args = (name,email,city)
    query = "insert into student(name,email,city) values(%s,%s,%s)"
    cursor.execute(query,args)
    conn.commit()
    print("data inserted")
    conn.close()

n = input("enter your name")
e = input("enter your email")
c = input("enter your city")
InsertData(n,e,c)    
