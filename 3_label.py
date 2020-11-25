from tkinter import *

root = Tk()
root.title("Sample")
root.geometry("640x480")
root.resizable(True,True)

label1 = Label(root,text="Hello world")
label1.pack()

photo = PhotoImage(file="gui_basic/cat.png")
label2 = Label(root,image=photo)
label2.pack()

def change():
    label1.config(text="Changed Label")

    global photo2
    photo2=PhotoImage(file="gui_basic/dog.png")
    label2.config(image=photo2)

btn1 = Button(root,text="button1",command=change)
btn1.pack()

root.mainloop()