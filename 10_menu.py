from tkinter import *

root = Tk()
root.title("Sample")
root.geometry("640x480")
root.resizable(False,False)

def newFile():
    print("New File")

menu = Menu(root)
# File メニュー
menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="New file",command=newFile)
menu_file.add_command(label="New Window")
# ライン表示
menu_file.add_separator()
menu_file.add_command(label="Open File...")
# 非活性
menu_file.add_command(label="Save All",state="disable")
menu.add_cascade(label="File",menu=menu_file)

menu_lang = Menu(menu,tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language",menu=menu_lang)

menu_view=Menu(menu,tearoff=0)
menu_view.add_checkbutton(label="Show")
menu.add_cascade(label="View",menu=menu_view)

root.config(menu=menu)
root.mainloop()