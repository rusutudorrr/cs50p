def math_interpreter():

    expression = input("Expression: ")

    x, y, z = expression.split(" ")

    if "+" in expression:
        addition = float(x) + float(z)
        print(addition)
    elif "-" in expression:
        minus = float(x) - float(z)
        print(minus)
    elif "*" in expression:
        multiplication = float(x) * float(z)
        print(multiplication)
    else:
        division = float(x) / float(z)
        print(division)


math_interpreter()