
# check button

from tkinter import*

root=Tk()
root.title("first gui")  
root.geometry("700x500+0+0")   # for give sixe to the window (widthxheight+from y+ from x)
root.wm_iconbitmap()  # you can put here the path of the icon or picture

def check_button_value():
    text1 = check_Button_var.get()
    lbl1.config(text=str(text1))

    text2 = check_Button_var1.get()
    lbl2.config(text=str(text2))



#label
lbl1 =  Label(root,text=" ",font=("arial",13,'bold'))
lbl1.place(x=50,y=300) 

lbl2 =  Label(root,text=" ",font=("arial",13,'bold'))
lbl2.place(x=50,y=400) 

# variable
check_Button_var = IntVar()
check_Button_var1 = StringVar()

# check button
check_btn = Checkbutton(root,variable=check_Button_var,onvalue=1,offvalue=0,text="Do you agree", font=("arial",13,"bold"))
check_btn.place(x=50,y=50)
check_Button_var.set('0')

check_btn = Checkbutton(root,variable=check_Button_var1,onvalue="on",offvalue="off",text="Do you agree", font=("arial",13,"bold"))
check_btn.place(x=50,y=100)
check_Button_var.set('off')

# normal button
btn = Button(root,text="click me", font=("arial",15,"bold"),command=check_button_value)
btn.place(x=50, y=200)

root.mainloop()  # it is to holf the window on screen
