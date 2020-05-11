from tkinter import *

#First Window Needed for any tkinter program
#Main window Creation

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#set a Default
# e.insert(0, "Enter Name")

def click_action():
    mylabel = Label(root, text="Hello " + e.get())
    mylabel.pack()

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)
    global symbol
    symbol = None
    global f_num
    f_num = None

def button_add():
    global f_num
    f_num = int(e.get())
    e.delete(0, END)
    global symbol
    symbol = "add"

def button_equal():
    s_num = int(e.get())
    e.delete(0, END)
    if symbol == "add":
        e.insert(0, f_num + s_num)


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), fg="blue", bg="#ffffff")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), fg="blue", bg="#ffffff")
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), fg="blue", bg="#ffffff")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), fg="blue", bg="#ffffff")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), fg="blue", bg="#ffffff")
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), fg="blue", bg="#ffffff")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), fg="blue", bg="#ffffff")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), fg="blue", bg="#ffffff")
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), fg="blue", bg="#ffffff")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), fg="blue", bg="#ffffff")

button_add = Button(root, text="+", padx=40, pady=20, command=button_add, fg="blue", bg="#ffffff")
button_equal = Button(root, text="=", padx=139, pady=20, command=button_equal, fg="blue", bg="#ffffff")
button_clr = Button(root, text="Clear", padx=30, pady=20, command=button_clear, fg="blue", bg="#ffffff")

#put the buttons on the screen
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_add.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_clr.grid(row=4, column=2)

button_equal.grid(row=5, column=0, columnspan=3)

root.mainloop()