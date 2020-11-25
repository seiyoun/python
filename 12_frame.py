from tkinter import *

root = Tk()
root.title("Sample")
root.geometry("640x480")
root.resizable(False,False)

Label(root,text="Sample").pack(side="top")

frame_burger = Frame(root,relief="solid",bd=1)
# side=位置 fill=全体 expandh=広げる
frame_burger.pack(side="left",fill="both",expand=True)

Button(frame_burger,text="A").pack()
Button(frame_burger,text="B").pack()
Button(frame_burger,text="C").pack()

frame_drink=LabelFrame(root,text="飲み物")
frame_drink.pack(side="right",fill="both",expand=True)
Button(frame_drink,text="A").pack()
Button(frame_drink,text="B").pack()
Button(frame_drink,text="C").pack()

root.mainloop()