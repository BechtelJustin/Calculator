def Calculator():
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
        print(int(a)/int(b))


Calculator()


def question():
    print("Continue?")
    input("yes or no?: ")
    yes = 1
    no = 2
    if 1:
        Calculator()
    if 2:
        print("Bye, bye")


question()
