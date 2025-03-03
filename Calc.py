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
if c is "/":
    print(int(a)/int(b))
