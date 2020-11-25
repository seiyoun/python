import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Sample")
root.geometry("640x480")
root.resizable(False,False)

var = DoubleVar()
progressbar = ttk.Progressbar(root,maximum=100,length=150,mode="determinate",variable=var)
#progressbar.start(10)
progressbar.pack()

def start():
    #progressbar.stop() 
    for i in range(0,101):
        # 0.01秒待機
        time.sleep(0.01) 
        # 値設定
        var.set(i)
        # 描画更新
        progressbar.update()

btn = Button(root,text="button",command=start)
btn.pack()

root.mainloop()