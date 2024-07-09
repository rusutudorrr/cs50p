from random import randint


def main():
    user_level = get_level()
    generate_integer(user_level)


def get_level():

    level = [1, 2, 3]

    while True:
        try:
            user_level = int(input())
            if user_level in level:
                return user_level
            else:
                raise ValueError("Must type 1, 2, or 3.")
        except ValueError:
            print("Must type 1, 2, or 3.")
            continue


def generate_integer(level):

    xy_counter = 1
    EEE_counter = 1



    while xy_counter != 10:
        try:
            if level == 1:
                x = randint(0, 9)
                y = randint(0, 9)
            elif level == 2:
                x = randint(10, 99)
                y = randint(10, 99)
            elif level == 3:
                x = randint(100, 999)
                y = randint(100, 999)

            z = x + y
            user_input = int(input(f"{x} + {y} = "))

            if user_input == z:
                xy_counter += 1


            while user_input != z:
                print("EEE")
                EEE_counter += 1
                if EEE_counter <= 3:
                    current_xy = (x, y)
                    user_input = int(input(f"{current_xy[0]} + {current_xy[1]} = "))
                else:
                    xy_counter += 1
                    print(f"{x} + {y} = {z}")
                    break

        except ValueError:
            print("EEE")


if __name__ == "__main__":
    main()