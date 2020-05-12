from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("How To Add Images To tkinter")
# root.iconbitmap("e-learning-monitor.1.svg")

myimage = ImageTk.PhotoImage(Image.open("sword.jpg"))
mylabel = Label(image=myimage)
mylabel.pack()


root.mainloop()