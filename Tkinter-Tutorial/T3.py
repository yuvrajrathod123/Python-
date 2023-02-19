
# how to create buttton and entry(input field)

from tkinter import*

root=Tk()
root.title("first gui")  
root.geometry("700x500+0+0")   # for give sixe to the window (widthxheight+from y+ from x)
root.wm_iconbitmap()  # you can put here the path of the icon or picture


# button
def click():
                     # here we will entry data #
    lbl1= Label(root,text="Button clicked "+ entry1.get(), font=("arial",15,"bold"))
    lbl1.pack()


Mybtn = Button(root,text="click me", font=("arial",22,"bold"),fg='white',bg='black',command=click)
Mybtn.place(x=50,y=100)


# entry
entry1=Entry(root,width=50,font=("arial",10),bg="red",fg="black")
entry1.place(x=0,y=10,relwidth=1)

root.mainloop()  # it is to holf the window on screen
