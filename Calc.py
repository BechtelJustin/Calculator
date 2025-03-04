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


def calculator():
    number_1 = (input("Enter first number: "))
    if number_1.isdigit():
        number_1 = float(number_1)
    else:
        print("Dumbass")
    number_2 = (input("Enter second number: "))
    if number_2.isdigit():
        number_2 = float(number_2)
    else:
        print("Dumbass")
    calculation = input("+, -, *, /: ")
    if calculation == "+":
        print(number_1+number_2)
    if calculation == "-":
        print(number_1-number_2)
    if calculation == "*":
        print(number_1*number_2)
    if calculation == "/":
        if number_1 == 0:
            print("cannot divide by 0")
            calculator()
        elif number_2 == 0:
            print("cannot divide by 0")
            calculator()
        else:
            print(number_1/number_2)
    question_1()


calculator()

# make error codes for if someone puts in a word for number_1 or 2 then send them back to enter the number
# fix /, 0/100 should = 0
# Python check is a number
