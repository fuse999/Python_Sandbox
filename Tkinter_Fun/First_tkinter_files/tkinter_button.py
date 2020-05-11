from tkinter import *

#First Window Needed for any tkinter program
#Main window Creation
root = Tk()

def click_action():
    mylabel = Label(root, text="You clicked the button!!!").pack()

mybutton = Button(root, text="Click me", padx=50, pady=50, command=click_action, fg="blue", bg="#ffffff").pack()

root.mainloop()
