from tkinter import*

root=Tk()
root.title("first gui")  
root.geometry("700x500+0+0")   # for give sixe to the window (widthxheight+from y+ from x)
root.wm_iconbitmap()  # you can put here the path of the icon or picture


# to create albel

# lbl1 = Label(root,text="Yuvraj rathod", font=("Times new roman",30,"bold"))
# to display the label on the screen
# lbl1.pack(side=TOP)

# Grid
# lbl1 = Label(root,text="Yuvraj", font=("Times new roman",30,"bold"))
# lbl1.grid(row=0,column=0)

# lbl1 = Label(root,text="Yuvi", font=("Times new roman",30,"bold"))
# lbl1.grid(row=0,column=1)

# lbl1 = Label(root,text="jay", font=("Times new roman",30,"bold"))
# lbl1.grid(row=1,column=0)

# place
lbl1 = Label(root,text="Yuvraj", font=("Times new roman",30,"bold"))
lbl1.place(x=100,y=100)



root.mainloop()  # it is to holf the window on screen
