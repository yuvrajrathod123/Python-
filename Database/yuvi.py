
import pymysql

def CreatConn():
    return pymysql.connect(host="localhost",database="lernvern",user="root",password="Yuvraj@5587",port=3306)