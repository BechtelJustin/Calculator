print("Welcome to calculator")


def question_1():
    print("Continue?")
    i = input("Yes or No?: ").lower()
    if (i) == "yes":
        calculator()

    if (i) == "no":
        print("Bye, bye")

    else:
        question_1()


def number_1():
    number_1v = (input("Enter first number: "))
    print(number_1v)
    return number_1v


def number_2():
    number_2v = (input("Enter second number: "))
    print(number_2v)
    return number_2v


def calculator():

    number_1v = number_1()
    while not number_1v.isdigit():
        print((number_1v), "Is not valid number")
        number_1v = number_1()
    number_1v = float(number_1v)

    calculation = input("+, -, *, /: ")

    number_2v = number_2()
    while not number_2v.isdigit():
        print((number_2v), "Is not valid number")
        number_2v = number_2()
    number_2v = float(number_2v)

    if calculation == "+":
        print(number_1v+number_2v)

    if calculation == "-":
        print(number_1v-number_2v)

    if calculation == "*":
        print(number_1v*number_2v)

    if calculation == "/":
        if number_1v == 0:
            print("cannot divide by 0")
            calculator()

        elif number_2v == 0:
            print("cannot divide by 0")
            calculator()

        else:
            print(number_1v/number_2v)

    question_1()


calculator()

# make error codes for if someone puts in a word for number_1 or 2 then send them back to enter the number
# made it restart from the start would like to send back to whatever step they were on before
# fix /, 100/0 should = 0
