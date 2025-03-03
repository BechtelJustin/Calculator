def question():
    print("Continue?")
    i = input("yes = 1 or no = 0?: ")
    while (float(i) > 0):
        calculator()
    print("Bye, bye")


def calculator():
    print("Welcome to calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = input("+, -, *, /")
    if c == "+":
        print(a+b)
    if c == "-":
        print(a-b)
    if c == "*":
        print(a*b)
    if c == "/":
        if a == 0:
            a1010()
        elif b == 0:
            a1010()
        else:
            print(a/b)
    question()


def a1010():
    print("Cannot Divide 0")
    calculator()


calculator()
