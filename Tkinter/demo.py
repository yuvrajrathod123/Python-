
from tkinter  import*



# createing main window
r = Tk()
# geometry method decide the size of the window in bot y axis and x axis
r.geometry("500x500")
# to give the title of the page
r.title("First App")
# r.minsize(100,100)
# r.minsize(1000,1000)
r.configure(bg="lightblue")

def  submit():
    print("button is clicked")
    submit_output.delete(0.0,END)
    if password_entry.get() != "" and username_entry.get() != "":
        val = "Loggin in..."
        submit_output.insert(END,val)
        username_entry.delete(0,END)
        password_entry.delete(0,END)
    
    else:
        val = "Invalid Entry"
        submit_output.insert(END,val)
    print(val)
       
# username
username_lbl = Label(text="Username",font=("arial",10,"bold"),bg='white')
username_lbl.grid(row=0,column=0,padx=10,pady=7)

username_entry = Entry(width=20,font=("arial",10,"bold"))
username_entry.grid(row=0,column=1,padx=0)

        
password_lbl = Label(text="password",font=("arial",10,"bold"),bg='white')
password_lbl.grid(row=1,column=0,padx=10,pady=7)

password_entry = Entry(width=20,font=("arial",10,"bold"))
password_entry.grid(row=1,column=1,padx=0)

button1 = Button(text=("submit"))
button1.grid(row=2, column=1, padx=0,pady=10)

#adding button
submit_button = Button(text="Submit", bg="white",c)

#displaying output of submit button
submit_output = Text(width=50,fg="white",bg="#333", borderwidth=0)
submit_output.pack(anchor=W)


        




# mainloop method  called  (main loop is for display the window on the screen)
r.mainloop()