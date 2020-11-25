from tkinter import *

root = Tk()
root.title("Sample")
root.geometry("640x480")
root.resizable(True,True)

# 
txt = Text(root,width=30,height=5)
txt.pack()
txt.insert(END,"Text Insert Test")

e=Entry(root,width=30)
e.pack()
e.insert(END,"Entry Insert Test")

def click():
    # 内容出力
    print(txt.get("1.0",END))
    print(e.get())

    # 内容削除
    txt.delete("1.0",END)
    e.delete(0,END)

btn = Button(root,text="Button1",command=click)
btn.pack()

root.mainloop()