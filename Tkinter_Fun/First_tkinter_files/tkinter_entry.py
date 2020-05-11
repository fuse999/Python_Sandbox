from tkinter import *

#First Window Needed for any tkinter program
#Main window Creation
root = Tk()

e = Entry(root, width=20)
e.pack()
#set a Default
# e.insert(0, "Enter Name")

def click_action():
    mylabel = Label(root, text="Hello " + e.get())
    mylabel.pack()

mybutton = Button(root, text="Submit Name", padx=10, pady=5, command=click_action, fg="blue", bg="#ffffff")
mybutton.pack()

root.mainloop()