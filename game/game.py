from random import randint


def main():
    random_number = guessing_level()
    guessing_game(random_number)


def guessing_level():

    while True:
        try:
            user_level = int(input("Level: "))
            random_number = randint(1, user_level)
        except ValueError:
            print("Must type a number.")
            continue

        return random_number


def guessing_game(random_number):

    while True:
        try:
            user_input = int(input("Guess: "))

            if user_input == random_number:
                print("Just right!")
                return random_number
            elif user_input > random_number:
                print("Too large!")
            elif user_input < random_number:
                print("Too small!")
            continue

        except ValueError:
            print("Must type a number.")


        except EOFError:
            break


main()
