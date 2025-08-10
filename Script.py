import math as m

a = "Enter first number "
b = "Enter second number "
c = "Enter the number "
q = "sqrt "
e = "squareroot "


def add(i, r):
    i+r
    print(i+r)


def sub(i, r):
    i-r
    print(i-r)


def div(i, r):
    if r == 0:
        print(i)
    else:
        print(i/r)


def mul(i, r):
    i*r
    print(i*r)


def power(i, r):
    m.pow(i, r)
    print(int(m.pow(i, r)))


def squareroot(i):
    m.sqrt(i)
    print(m.sqrt(i))


def helpfacility():
    print("Welcome to the help facility! \n"
          "you can type any mathematical opration that you want to perform for example:-"
          " add in the prompt right in front of 'Enter command' ")


while True:
    command = input("Enter command- ")

    if "stop" in command:
        break

    elif 'exit' in command:
        break

    elif "help" in command:
        helpfacility()

    elif "add" in command:
        add(int(input(a)), int(input(b)))

    elif "sub" in command:
        sub(int(input(a)), int(input(b)))

    elif "div" in command:
        div(int(input(a)), int(input(b)))

    elif "mul" in command:
        mul(int(input(a)), int(input(b)))

    elif "pow" in command:
        pow(int(input(a)), int(input(b)))

    elif e in command:
        squareroot(int(input(c)))

    elif q in command:
        squareroot(int(input(c)))

    else:
        print("I am unable to understand.")
