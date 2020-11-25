from tkinter import *

root = Tk()
root.title("Sample")
root.geometry("640x480")
root.resizable(True,True)

txt = Text(root,width=30,height=5)
txt.pack()

txt.insert(END,"Insert Test")

root.mainloop()