def main():

    fuel("Fraction: ")


def fuel(prompt: str):

    while True:
        try:
            user_input = input(prompt)
            x = int(user_input.split("/")[0])
            y = int(user_input.split("/")[1])
            if x > y:
                print("Numerator cannot be greater than denominator")
                continue
            percentage = round(x / y * 100)
            if percentage in [0, 1]:
                print("E")
            elif percentage in [99, 100]:
                print("F")
            else:
                print(F"{percentage}%")

            return percentage

        except ValueError:
            print("Your values are not correct")
        except ZeroDivisionError:
            print("Cannot divide by 0")


if __name__ == "__main__":
    main()
