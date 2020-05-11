from tkinter import *

#First Window Needed for any tkinter program
#Main window Creation
root = Tk()

#Creating Label widget
mylabel1 = Label(root, text="Hello World!").grid(row=0, column=0)

mylabel2 = Label(root, text="My name is Riley Pence")

#shoving it on the screen
mylabel2.grid(row=1, column=0)


root.mainloop()
