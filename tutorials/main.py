from tkinter import *

root = Tk()

label1 = Label(root, text = "Hello World 1 ")
label2 = Label(root, text = "Hello World 2 ")
label1.grid(row=0, column = 0)
label2.grid(row=1, column = 1)





root.title("Posts page")
#root.geometry("1920x1080")
root.mainloop()