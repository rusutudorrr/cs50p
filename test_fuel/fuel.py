def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except ValueError:
        print("Invalid input. Please enter a fraction in the format x/y.")


def convert(fraction):
    x, y = map(int, fraction.split("/"))

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")

    if x > y:
        raise ValueError("Numerator cannot be greater than denominator")

    return round(x / y * 100)


def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()
