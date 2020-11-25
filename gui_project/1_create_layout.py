from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Sample")
root.geometry("640x530")
root.resizable(False,False)

# file Frame
file_frame = Frame(root)
file_frame.pack(fill="x",padx=5,pady=5)

btn_add_file = Button(file_frame,width=15,height=1,text="ファイル追加")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame,width=15,height=1,text="ファイル削除")
btn_del_file.pack(side="right")

# list Frame
list_frame = Frame(root)
list_frame.pack(fill="both",padx=5,pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file=Listbox(list_frame,selectmode="extended",height=15,yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)

scrollbar.config(command=list_file.yview)

# save path Frame
path_frame=LabelFrame(root,text="save path")
path_frame.pack(fill="x",padx=5,pady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left",fill="both",expand=True,padx=5,pady=5)

btn_dest_path = Button(path_frame,text="Open", width=10)
btn_dest_path.pack(side="right",padx=5,pady=5)

# option Frame
option_frame = LabelFrame(root,text="Option")
option_frame.pack(fill="x",padx=5,pady=5)

# サイズ
label_size=Label(option_frame,text="size",width=10)
label_size.pack(side="left")

option_size=["default","1024","800","640"]
cmb_size = ttk.Combobox(option_frame,state="readonly",values=option_size,width=10)
cmb_size.current(0)
cmb_size.pack(side="left")

# 間隔
label_space=Label(option_frame,text="space",width=10)
label_space.pack(side="left",padx=5,pady=5)

option_space=["None","small","medium","big"]
cmb_space = ttk.Combobox(option_frame,state="readonly",values=option_space,width=10)
cmb_space.current(0)
cmb_space.pack(side="left",padx=5,pady=5)

# フォーマット
label_format=Label(option_frame,text="format",width=10)
label_format.pack(side="left",padx=5,pady=5)

option_format=["PNG","JPG","BMP"]
cmb_format = ttk.Combobox(option_frame,state="readonly",values=option_format,width=10)
cmb_format.current(0)
cmb_format.pack(side="left")

#progressbar
frame_progress=LabelFrame(root,text="Progress")
frame_progress.pack(fill="x",padx=5,pady=5)

p_var = DoubleVar()
progressbar = ttk.Progressbar(frame_progress,maximum=100,variable=p_var)
progressbar.pack(fill="x",padx=5,pady=5)

#run
frame_run = Frame(root)
frame_run.pack(fill="x",padx=5,pady=5)

btn_close = Button(frame_run,text="Close",width=15)
btn_close.pack(side="right",padx=5,pady=5)

btn_start = Button(frame_run,text="Start",width=15)
btn_start.pack(side="right",padx=5,pady=5)

root.mainloop()