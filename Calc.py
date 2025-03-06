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
    return number_1v


def calculation():
    calculation_s = input("+, -, *, /: ")
    return calculation_s


def number_2():
    number_2v = (input("Enter second number: "))
    return number_2v


def calculator():

    number_1v = number_1()
    while not number_1v.isdigit() and number_1v.isdecimal():
        print((number_1v), "Is not valid number")
        number_1v = number_1()
    number_1v = float(number_1v)

    calculation_s = calculation()
    symbol_count = calculation_s

    number_2v = number_2()
    while not number_2v.isdigit() and number_2v.isdecimal():
        print((number_2v), "Is not valid number")
        number_2v = number_2()
    number_2v = float(number_2v)

    while calculator:
        symbol_count = len(calculation_s.split("+"))-1
        symbol_count = int(symbol_count)
        if symbol_count == 1:
            print(number_1v+number_2v)
            break

        symbol_count = len(calculation_s.split("-"))-1
        symbol_count = int(symbol_count)
        if symbol_count == 1:
            print(number_1v-number_2v)
            break

        symbol_count = len(calculation_s.split("*"))-1
        symbol_count = int(symbol_count)
        if symbol_count == 1:
            print(number_1v*number_2v)
            break

        symbol_count = len(calculation_s.split("/"))-1
        symbol_count = int(symbol_count)
        if symbol_count == 1:
            if number_2v == 0 or number_1v == 0 and number_2v == 0:
                print("cannot divide by 0")
            else:
                print(number_1v/number_2v)
                break

    question_1()


print("Welcome to calculator")
calculator()


# somehow find out how to get it to minus when doing -+
