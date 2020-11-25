from tkinter import *

root = Tk()
root.title("Sample")
root.geometry("640x480")
root.resizable(False,False)

label1 = Label(root,text="選択してください")
label1.pack()

radiovar=IntVar()
radiobutton1 = Radiobutton(root,text="A",value=1,variable=radiovar)
radiobutton2 = Radiobutton(root,text="B",value=2,variable=radiovar)
radiobutton3 = Radiobutton(root,text="C",value=3,variable=radiovar)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

# デフォルト選択
radiobutton1.select()

label2 = Label(root,text="String選択してください")
label2.pack()

radiovar2=StringVar()
radiobutton4 = Radiobutton(root,text="A",value="A",variable=radiovar2)
radiobutton5 = Radiobutton(root,text="B",value="B",variable=radiovar2)
radiobutton6 = Radiobutton(root,text="C",value="C",variable=radiovar2)
radiobutton4.pack()
radiobutton5.pack()
radiobutton6.pack()

radiobutton4.select()

def click():
    # 選択中ラジオボタンvalueを取得
    print(radiovar.get())

    # 選択中ラジオボタンvalueを取得
    print(radiovar2.get())

btn = Button(root,text="button",command=click)
btn.pack()

root.mainloop()