import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image
import os

root = Tk()
root.title("Sample")
root.geometry("640x530")
root.resizable(False,False)

# ファイル選択
def add_file():
    # 選択ウィンドウを開く
    files = filedialog.askopenfilenames(title="ファイル選択",filetypes=(("PNG","*.png"),("All","*.*")))

    for file in files:
        print(file)
        list_file.insert(END,file)

# ファイル削除
def del_file():
    print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# セーブパス
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected is None:
        return
    
    print(folder_selected)
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0,folder_selected)

def merge_image():
    #print(list_file.get(0,END))
    images = [Image.open(x) for x in list_file.get(0,END)]

    # size[0]=width size[1]=height
    #widths = [x.size[0] for x in images]
    #height = [y.size[1] for y in images]

    widths,heights = zip(*(x.size for x in images))

    #print(widths)
    #print(height)

    max_width,total_height = max(widths),sum(heights)
    #print(max_width)
    #print(total_height)

    result_img = Image.new("RGB",(max_width,total_height),(255,255,255))
    y_offset = 0
    for idx,img in enumerate(images):
        result_img.paste(img,(0,y_offset))
        y_offset += img.size[1]

        progress = (idx + 1) / len(images) * 100
        p_var.set(progress)
        progressbar.update()

    dest_path = os.path.join(txt_dest_path.get(),"Test.png")
    result_img.save(dest_path)
    msgbox.showinfo("","成功しました")

# 実行
def start():
    print("size",cmb_size.get())
    print("space",cmb_space.get())
    print("format",cmb_format.get())

    if list_file.size() == 0:
        msgbox.showerror("Error","ファイルを追加してください")
        return

    if len(txt_dest_path.get()) == 0:
        msgbox.showerror("Error","保存先パスを設定してください")
        return

    merge_image()
    

# file Frame
file_frame = Frame(root)
file_frame.pack(fill="x",padx=5,pady=5)

btn_add_file = Button(file_frame,width=15,height=1,text="ファイル追加",command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame,width=15,height=1,text="ファイル削除",command=del_file)
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
path_frame=LabelFrame(root,text="Save path")
path_frame.pack(fill="x",padx=5,pady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left",fill="both",expand=True,padx=5,pady=5)

btn_dest_path = Button(path_frame,text="Open", width=10,command=browse_dest_path)
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

btn_start = Button(frame_run,text="Start",width=15,command=start)
btn_start.pack(side="right",padx=5,pady=5)

root.mainloop()