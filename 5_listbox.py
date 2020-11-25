from tkinter import *

root = Tk()
root.title("Sample")
root.geometry("640x480")
root.resizable(True,True)

listbox = Listbox(root,selectmode="extended",height=0)
# 項目追加
listbox.insert(0,"A")
listbox.insert(1,"B")
listbox.insert(2,"C")
listbox.insert(END,"D")
listbox.insert(END,"E")
listbox.pack()

def click():
    # 削除
    #listbox.delete(0)

    # 項目出力
    print(listbox.get(0,2))

    # 選択インデックス
    print(listbox.curselection())

    # リストボックスサイズ
    print(listbox.size())

btn = Button(root,text="Button1",command=click)
btn.pack()

root.mainloop()