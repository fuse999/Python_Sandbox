from tkinter import *

#First Window Needed for any tkinter program
#Main window Creation
root = Tk()

#Creating Label widget
mylabel = Label(root, text="Hello World!")

#shoving it on the screen
mylabel.pack()


root.mainloop()
