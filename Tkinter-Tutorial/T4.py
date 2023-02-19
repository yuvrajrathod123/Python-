from tkinter import*

root=Tk()
root.title("first gui")  
root.geometry("700x500+0+0")   # for give sixe to the window (widthxheight+from y+ from x)
root.wm_iconbitmap()  # you can put here the path of the icon or picture


# button
def click():
   text1 = "hello " + entry1.get() 
   lbl1.config(text=str(text1))
   

Mybtn = Button(root,text="click me", font=("arial",22,"bold"),fg='white',bg='black',command=click)
Mybtn.place(x=50,y=200)

# textfild
text_box = Text(root,font=("arial",10))
text_box.place(x=0,y=50,relwidth=0.5, relheight=0.20)

# entry
entry1=Entry(root,width=50,font=("arial",10),bg="red",fg="black")
entry1.place(x=0,y=10,relwidth=1)

# label
lbl1= Label(root,text=" "+ entry1.get(), font=("arial",15,"bold"))
lbl1.place(x=50,y=300)

root.mainloop()  # it is to holf the window on screenS
