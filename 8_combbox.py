import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Sample")
root.geometry("640x480")
root.resizable(False,False)

values = [str(i) + "日" for i in range(1,32)]

# hegith=項目数 readonly=読み込み専用
combbox = ttk.Combobox(root,height=10,values=values,state="readonly")
combbox.pack()
# デフォルト0番目選択
combbox.current(0)

def click():
    print(combbox.get())

btn =Button(root,text="button",command=click)
btn.pack()

root.mainloop()