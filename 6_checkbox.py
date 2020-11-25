from tkinter import *

root = Tk()
root.title("Sample")
root.geometry("640x480")
root.resizable(False,False)

chkvar = IntVar()
chkbox = Checkbutton(root,text="チェックボックス",variable=chkvar)
chkbox.pack()
# デフォルトチェック
#chkbox.select()
# チェック解除
#chkbox.deselect()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root,text="チェックボックス2",variable=chkvar2)
chkbox2.pack()

def click():
    # チェックボックス値を取得
    print(chkvar.get())

btn = Button(root,text="button",command=click)
btn.pack()

root.mainloop()