
from tkinter  import*
import pymysql
import tkinter.messagebox as m


# createing main window
r = Tk()
# geometry method decide the size of the window in bot y axis and x axis
r.geometry("500x500")
# to give the title of the page
r.title("First App")
# for background
r.configure(bg="lightblue")


# connection function
def CreateConn():
    return pymysql.connect(host="localhost",database="tkinter",user="root",password="Yuvraj@5587",port=3306)

def InsertData():
    r = ern.get()
    f = efn.get()
    l = eln.get()
    e = eemail.get()

    if( r=="" or f=="" or l=="" or e==""):
        m.showinfo("Insert status","All fields ara compulsory")
    else:
        try:
            conn = CreateConn()
            cursor = conn.cursor()
            args = (r,f,l,e)
            query = "Insert into students(rollno,fname,lname,email)values(%s,%s,%s,%s)"
            cursor.execute(query,args)
            m.showinfo("Insert status","data inserted")
            conn.close()
        except Exception as ee:
            print("Insert Exceprtion",ee)    
# ======= adding wintage to window =======

roll_no = Label(r,text="Roll No")
roll_no.place(x=20,y=20)      # place() is used to place the label on window

firstname = Label(r,text="First Name")
firstname.place(x=20,y=50)

lastname = Label(r,text="Last Name")
lastname.place(x=20,y=80)

email = Label(r,text="Email")
email.place(x=20,y=110)

# addinng entry box into main window
ern = Entry()
ern.place(x=100,y=20)
efn = Entry()
efn.place(x=100,y=50)
eln = Entry()
eln.place(x=100,y=80)
eemail = Entry()
eemail.place(x=100,y=110)

# andding buttons to main window

Button1 =  Button(r,text="Button1",bg="white",command=InsertData)
Button1.place(x=20,y=150)



# mainloop method  called  (main loop is for display the window on the screen)
mainloop()