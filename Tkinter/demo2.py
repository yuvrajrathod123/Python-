from tkinter import *

# Creating a new window
root = Tk()

# Setting window background color
root.configure(bg="#333333")

# Defining all function
def submit():
        submit_output.delete(0.0,END)
        if password_entry.get()  != "" and username_entry.get() != "":
                val = "Logging in..."
                submit_output.insert(END, val)
                username_entry.delete(0,END)
                password_entry.delete(0, END) 
        else :
                val = "Invalid entry"
                submit_output.insert(END,val)
        print(val)

# Setting default size of window (width x height)
root.geometry("400x400")
root.minsize(100,100) #min size of window (width, height)
# root.maxsize(1000,1000) #max size of window (width, height)


# Creating a label
label1 = Label(text="Hello User", fg="white", font=20, bg="#333", justify="left")
label1.pack(anchor=CENTER)

username_label = Label(text="Username",fg="white",bg="#333")
username_label.pack( anchor=CENTER)
username_entry = Entry(bg="white",fg="black")
username_entry.pack( anchor=CENTER)

password_label = Label(text="Password",fg="white",bg="#333")
password_label.pack(anchor=CENTER)
password_entry = Entry(show="*", bg="white",fg="black")
password_entry.pack(anchor=CENTER)

# Adding button
submit_button = Button(text="Submit", bg="white", fg="black", command=submit, justify="left")
submit_button.pack(pady=10, anchor=CENTER)

# Displaying output of submit button
submit_output = Text(width=50,fg="white",bg="#333", borderwidth=0)
submit_output.pack(anchor=CENTER)


def attendance(self): 
    self.new_window = Toplevel(self.root)
    self.app = (self.new_window)    

# Runs the program
root.mainloop()
