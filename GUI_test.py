from tkinter import *
from tkinter import ttk
import math as ma

a = "Enter first number"
b = "Enter second number"
c = "Enter the number"
q = "sqrt"
e = "squareroot"


def add():
    result = w.get() + s.get()
    print(result)
    ans.set(result)


def sub():
    result = w.get() - s.get()
    print(result)
    ans.set(result)


def div():
    result = w.get() / s.get()
    print(result)
    ans.set(result)


def mul():
    result = w.get() * s.get()
    print(result)
    ans.set(result)


def power():
    result = w.get() ** s.get()
    print(result)
    ans.set(result)


def squareroot():
    result = ma.sqrt(s.get())
    print(result)
    ans.set(result)


def helpfacility():
    print("Welcome to the help facility!"
          " \nyou can type any mathematical opration that you want to perform for example:-"
          " add in the prompt right in front of 'Enter command' ")


def calculate(*args):
    try:
        value = str(usr_input.get())
        print(value)
        if value == "add":
            add()

        elif value == "sub":
            sub()

        elif value == "div":
            div()

        elif value == "mul":
            mul()

        elif value == "power":
            power()

        elif value == "sqrt":
            squareroot()

        elif value == "help":
            helpfacility()

        else:
            print("command no valid \nif you don't know how to use the calculator use the help, to use help command "
                  "type help in the entry box")

    except ValueError:
        pass


root = Tk()
root.title("Calculator")

frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

usr_input = StringVar()
input_entry = ttk.Entry(frame, width=20, textvariable=usr_input)
input_entry.grid(column=2, row=1, sticky=(W, E))
ans = StringVar()
ttk.Label(frame, textvariable=ans).grid(column=2, row=2)

ttk.Button(frame, text="Calculate", command=calculate).grid(column=1, row=3)
ttk.Button(frame, text="exit", command=root.destroy).grid(column=3, row=3, sticky=(W, E))

w = IntVar()
s = IntVar()
ent_s = ttk.Entry(frame, width=10, textvariable=s)
ent_w = ttk.Entry(frame, width=10, textvariable=w)

ttk.Label(frame, text="your answer is =").grid(column=1, row=2)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

input_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
