def question():
    print("Continue?")
    i = input("yes = 1 or no = 0?: ")
    while (int(i) > 0):
        calculator()
    else:
        print("Bye, bye")


def calculator():
    print("Welcome to calculator")
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    c = input("+, -, *, /")
    if c == "+":
        print(int(a)+int(b))
    if c == "-":
        print(int(a)-int(b))
    if c == "*":
        print(int(a)*int(b))
    if c == "/":
        if int(a) == 0:
            a1010()
        elif int(b) == 0:
            a1010()
        else:
            print(int(a)/int(b))
    question()


def a1010():
    print("Cannot Divide 0")
    calculator()


calculator()
