
import pymysql

def CreatConn():
    return pymysql.connect(host="localhost",database="lernvern",user="root",password="Yuvraj@5587",port=3306)

# create table

def CreateTable():
    conn = CreatConn()
    cursor = conn.cursor()  #helps to execute query
    query = "create table student(sid int primary key auto_increment, name varchar(50), email varchar(50),city varchar(45))" 

    cursor.execute(query)
    conn.commit()  #to save the data into database
    print("table create")
    conn.close()

#calling create table method

CreateTable()    