from tkinter import *

root = Tk()
# タイトル
root.title("Sample")
# ウィンドウサイズ
root.geometry("640x480")
# ウィンドウサイズ変更
root.resizable(True,True)
# メニューバー
menu = Menu(root)
# メニュー
menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="Open")
menu_file.add_command(label="Save")
menu_file.add_command(label="Close",command=root.quit)
# メニューバーにFileを追加
menu.add_cascade(label="File", menu=menu_file)
# メニューバー設定
root.config(menu=menu)

# スクロールバー
scrollbar = Scrollbar(root)
scrollbar.pack(side="right",fill="y")

# テキスト入力
txt = Text(root,yscrollcommand=scrollbar.set)
txt.pack(side="left",fill="both",expand=True)

scrollbar.config(command=txt.yview)
root.mainloop()