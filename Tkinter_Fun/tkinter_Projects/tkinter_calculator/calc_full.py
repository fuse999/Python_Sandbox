from tkinter import *

#First Window Needed for any tkinter program
#Main window Creation

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

f = Label(root, text="Made By, Riley ")
f.grid(row=0, column=3)
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
    f_num = float(e.get())
    e.delete(0, END)
    global symbol
    symbol = "add"

def button_sub():
    global f_num
    f_num = float(e.get())
    e.delete(0, END)
    global symbol
    symbol = "sub"

def button_multi():
    global f_num
    f_num = float(e.get())
    e.delete(0, END)
    global symbol
    symbol = "multi"

def button_dev():
    global f_num
    f_num = float(e.get())
    e.delete(0, END)
    global symbol
    symbol = "dev"

def button_pn():
    current = e.get()
    if float(current) > 0:
        e.delete(0, END)
        e.insert(0, "-" + str(current))
    else:
        current = current[1:]
        e.delete(0, END)
        e.insert(0, str(current))

def button_dec():
    current = e.get()
    if "." not in str(current):
        e.delete(0, END)
        e.insert(0, str(current).join("."))

def button_bksp():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current[:-1]))

def add_memory():
    global memory_value
    memory_value = e.get()

def use_memory():
    if memory_value != None:
        e.delete(0, END)
        e.insert(0, str(memory_value))

def button_clr_all():
    e.delete(0, END)
    global symbol
    symbol = None
    global f_num
    f_num = None
    global memory_value
    memory_value = None

def button_equal():
    s_num = float(e.get())
    e.delete(0, END)
    if symbol == "add":
        e.insert(0, f_num + s_num)
    if symbol == "sub":
        e.insert(0, f_num - s_num)
    if symbol == "multi":
        e.insert(0, f_num * s_num)
    if symbol == "dev":
        e.insert(0, f_num / s_num)


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
button_sub = Button(root, text="-", padx=40, pady=20, command=button_sub, fg="blue", bg="#ffffff")
button_multi = Button(root, text="*", padx=40, pady=20, command=button_multi, fg="blue", bg="#ffffff")
button_dev = Button(root, text="/", padx=40, pady=20, command=button_dev, fg="blue", bg="#ffffff")

button_pn = Button(root, text="-/+", padx=34, pady=20, command=button_pn, fg="blue", bg="#ffffff")
button_dec = Button(root, text=".", padx=42, pady=20, command=button_dec, fg="blue", bg="#ffffff")

button_equal = Button(root, text="=", padx=135, pady=20, command=button_equal, fg="blue", bg="#ffffff")
button_clr = Button(root, text="C", padx=39, pady=20, command=button_clear, fg="blue", bg="#ffffff")
button_clr_all = Button(root, text="MC", padx=35, pady=20, command=button_clr_all, fg="blue", bg="#ffffff")
button_bksp = Button(root, text="Bksp", padx=32, pady=20, command=button_bksp, fg="blue", bg="#ffffff")
button_add_mem = Button(root, text="M+", padx=34, pady=20, command=add_memory, fg="blue", bg="#ffffff")
button_use_mem = Button(root, text="M", padx=37, pady=20, command=use_memory, fg="blue", bg="#ffffff")

#put the buttons on the screen
button_use_mem.grid(row=1, column=0)
button_clr_all.grid(row=1, column=1)
button_clr.grid(row=1, column=2)
button_bksp.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_add.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_multi.grid(row=4, column=3)

button_pn.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_dec.grid(row=5, column=2)
button_dev.grid(row=5, column=3)

button_equal.grid(row=6, column=0, columnspan=3)
button_add_mem.grid(row=6, column=3)

root.mainloop()