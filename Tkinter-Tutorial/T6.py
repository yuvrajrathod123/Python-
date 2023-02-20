
# Radio buttton in tkinter

from tkinter import*

root=Tk()
root.title("first gui")  
root.geometry("700x500+0+0")   # for give sixe to the window (widthxheight+from y+ from x)
root.wm_iconbitmap()  # you can put here the path of the icon or picture

# function
def get_gender():
    text1 = gender.get() 
    lbl1.config(text=str(text1))

# label
lbl1= Label(root,text=" ", font=("arial",15,"bold"))
lbl1.place(x=50,y=200)

# radio button
gender=StringVar()
male = Radiobutton(root,variable=gender,value="male",text="male", font=("arial",12,"bold"))
male.place(x=50,y=50)
gender.set("male")

female = Radiobutton(root,variable=gender,value="female",text="female", font=("arial",12,"bold"))
female.place(x=200,y=50)

# simple button
btn=Button(root,text="click here",font=("arial",12,"bold"),fg="white",bg="black",command=get_gender)
btn.place(x=100,y=100)

root.mainloop()  # it is to holf the window on screen


