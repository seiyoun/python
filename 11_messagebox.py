from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("Sample")
root.geometry("640x480")
root.resizable(False,False)

# 情報
def info():
    msgbox.showinfo("確認","成功")
btn= Button(root,command=info,text="通知")
btn.pack()

# 警告
def warning():
    msgbox.showwarning("確認","警告")
Button(root,command=warning,text="警告").pack()

# エラー
def error():
    msgbox.showerror("確認","エラー")
Button(root,command=error,text="エラー").pack()

# OK/Cancel
def okcancel():
    msgbox.askokcancel("確認","テスト")
Button(root,command=okcancel,text="ok/cancel").pack()

# Retry/Cancel
def retryCancel():
    msgbox.askretrycancel("確認","テスト")
Button(root,command=retryCancel,text="retry/cancel").pack()

# YES/NO/Cancel
def yesnocancel():
    response = msgbox.askyesnocancel("確認","テスト")
    if response == 1:
        print("Yes")
    elif response == 0:
        print("No")
    else:
        print("Cancel")
Button(root,command=yesnocancel,text="yes/no/cancel").pack()

root.mainloop()