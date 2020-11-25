from tkinter import *

root = Tk()
root.title("Sample")
root.geometry("640x480")
root.resizable(True,True)

btn1 = Button(root,text="button1")
btn1.pack()

btn2 = Button(root,padx=5,pady=10, text="button2")
btn2.pack()

btn3 = Button(root,width=5,height=3, text="button3")
btn3.pack()

btn4 = Button(root,fg="red",bg="yellow",text="button4")
btn4.pack()

photo = PhotoImage(file="gui_basic/cat.png")
btn5=Button(root,image=photo,text="buttn5")
btn5.pack()

def btncmd():
    print("On Click")

btn6 = Button(root,text="button6",command=btncmd)
btn6.pack()

root.mainloop()