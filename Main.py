from tkinter import *
from tkinter import ttk
import math
import cv2

m = ""


def add():
    value = usr_input.get()
    main = value.split()
    print("i have to add")
    d = int(main[0])
    b = int(main[2])
    global m
    m = d + b
    print(m)
    result.set(m)
    usr_input.set(m)


def sub():
    value = usr_input.get()
    main = value.split()
    print("i have to substract")
    d = int(main[0])
    b = int(main[2])
    global m
    m = d - b
    print(m)
    result.set(m)
    usr_input.set(m)


def div():
    value = usr_input.get()
    main = value.split()
    print("i have to divide")
    d = int(main[0])
    b = int(main[2])
    global m
    m = d / b
    print(m)
    result.set(m)
    usr_input.set(m)


def mul():
    value = usr_input.get()
    main = value.split()
    print("i have to multiply")
    d = int(main[0])
    b = int(main[2])
    global m
    m = d * b
    print(m)
    result.set(m)
    usr_input.set(m)


def power():
    value = usr_input.get()
    main = value.split()
    d = int(main[0])
    b = int(main[2])
    global m
    m = d ** b
    print(m)
    result.set(m)
    usr_input.set(m)


def squareroot():
    value = usr_input.get()
    main = value.split()
    print("i have give the squareroot of the given number")
    d = int(main[0])
    global m
    m = math.sqrt(d)
    print(m)
    result.set(m)
    usr_input.set(m)


def help_cal():
    r = "Welcome to the help facility for Calculator! \nyou can perform any mathematical" \
        " opration in this calculator, but this calculator program is under development .\n" \
        "so , if you feel any lack of comfort so please inform us in feedback."
    print(r)


def press_num(num):
    global m
    m = m + str(num)
    usr_input.set(m)
    print(m)


def clear():
    global m
    m = ''
    usr_input.set(m)


def listostr(s):
    str1 = " "
    return(str1.join(s))


def delete_one():
    global m
    j = m.split()
    print(j)
    j.pop(-1)
    print(j)
    g = listostr(j)
    print(g)
    usr_input.set(g)
    m = g + ' '


def decimal():
    press_num('.')
    s = eval(str(m))
    usr_input.set(s)


def calculate():
    try:
        value = usr_input.get()
        main = value.split()
        if main[1] == '+':
            add()
            global m
            m = ''

        elif main[1] == '-':
            sub()
            m = ''

        elif main[1] == '*':
            mul()
            m = ''

        elif main[1] == '/':
            div()
            m = ''

        elif main[1] == 'sqrt':
            squareroot()
            m = ''

        elif main[1] == 'power':
            power()
            m = ''

    except ValueError:
        pass


a = 15
root = Tk()
root.title("Calculator")
root.grid(1000, 1000, 200, 400)

frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

usr_input = StringVar()
usr_entry = ttk.Entry(frame, textvariable=usr_input )
usr_entry.insert(0,"Enter Number")
usr_entry.grid(columnspan=4, row=1, ipadx=140, ipady=15)

result = StringVar()

ttk.Button(frame, width=a, text="exit", command=root.destroy).grid(column=2, row=6, ipady=a)
ttk.Button(frame, width=a, text="=", command=calculate).grid(column=3, row=6, ipady=a)
ttk.Button(frame, width=a, text="1", command=lambda: press_num(1)).grid(column=0, row=2, ipady=a)
ttk.Button(frame, width=a, text="2", command=lambda: press_num(2)).grid(column=1, row=2, ipady=a)
ttk.Button(frame, width=a, text="3", command=lambda: press_num(3)).grid(column=2, row=2, ipady=a)
ttk.Button(frame, width=a, text="4", command=lambda: press_num(4)).grid(column=0, row=3, ipady=a)
ttk.Button(frame, width=a, text="5", command=lambda: press_num(5)).grid(column=1, row=3, ipady=a)
ttk.Button(frame, width=a, text="6", command=lambda: press_num(6)).grid(column=2, row=3, ipady=a)
ttk.Button(frame, width=a, text="7", command=lambda: press_num(7)).grid(column=0, row=4, ipady=a)
ttk.Button(frame, width=a, text="8", command=lambda: press_num(8)).grid(column=1, row=4, ipady=a)
ttk.Button(frame, width=a, text="9", command=lambda: press_num(9)).grid(column=2, row=4, ipady=a)
ttk.Button(frame, width=a, text="0", command=lambda: press_num(0)).grid(column=1, row=5, ipady=a)
ttk.Button(frame, width=a, text="/", command=lambda: press_num(' / ')).grid(column=3, row=2, ipady=a)
ttk.Button(frame, width=a, text="*", command=lambda: press_num(' * ')).grid(column=3, row=3, ipady=a)
ttk.Button(frame, width=a, text="+", command=lambda: press_num(' + ')).grid(column=3, row=4, ipady=a)
ttk.Button(frame, width=a, text="-", command=lambda: press_num(' - ')).grid(column=3, row=5, ipady=a)
ttk.Button(frame, width=a, text="sqrt", command=lambda: press_num(' sqrt ')).grid(column=0, row=5, ipady=a)
ttk.Button(frame, width=a, text="power", command=lambda: press_num(' power ')).grid(column=2, row=5, ipady=a)
ttk.Button(frame, width=a, text="clear", command=clear).grid(column=1, row=6, ipady=a)
ttk.Button(frame, width=a, text="Help", command=help_cal).grid(column=0, row=6, ipady=a)
ttk.Button(frame, width=a, text="del", command=delete_one).grid(column=0, row=7, ipady=a)
ttk.Button(frame, width=a, text=".", command=decimal).grid(column=1, row=7, ipady=a)

usr_entry.focus()

root.mainloop()