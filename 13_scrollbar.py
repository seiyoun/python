from tkinter import *

root = Tk()
root.title("Sample")
root.geometry("640x480")
root.resizable(False,False)

frame = Frame(root)
frame.pack()

#スクロールバー
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right",fill="y")

# リストボックスにスクロールバーを紐付け
listbox = Listbox(frame,selectmode="extended",height=10,yscrollcommand=scrollbar.set)
for i in range(1,32):
    listbox.insert(END,str(i)+"日")
listbox.pack(side="left")

# スクロールバーにリストを紐付ける
scrollbar.config(command=listbox.yview)

root.mainloop()