from tkinter import *

root = Tk()
root.title("Sample")
root.geometry("640x480")
root.resizable(False,False)

btn1 = Button(root,text="Button1")
# row 横 column 縦
btn1.grid(row=0,column=0)

btn2 = Button(root,text="Button2")
btn2.grid(row=0,column=1)

btn3 = Button(root,text="Button3")
# row=横 column=縦 columnspan=数分結合 sticky=四方向位置揃える
btn3.grid(row=1,column=0,columnspan=2,sticky=N+E+W+S)

btn4 = Button(root,text="Button4")
btn4.grid(row=2,column=0,sticky=N+E+W+S)

btn5 = Button(root,text="Button5")
btn5.grid(row=3,column=0,sticky=N+E+W+S)

btn6 = Button(root,text="Button6")
btn6.grid(row=2,column=1,rowspan=2,sticky=N+E+W+S)

root.mainloop()