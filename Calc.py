print("Welcome to calculator")


def question():
    print("Continue?")
    i = input("yes = 1 or no = 0?: ")
    while (float(i) > 0):
        calculator()
    print("Bye, bye")


def calculator():
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter second number: "))
    c = input("+, -, *, /")
    if c == "+":
        print(number_1+number_2)
    if c == "-":
        print(number_1-number_2)
    if c == "*":
        print(number_1*number_2)
    if c == "/":
        if number_1 == 0:
            errorcode_a1010()
        elif number_2 == 0:
            errorcode_a1010()
        else:
            print(number_1/number_2)
    question()


def errorcode_a1010():
    print("Cannot Divide 0")
    calculator()


calculator()

# make error codes for if someone puts in a word for number_1 or 2 then send them back to enter the number
