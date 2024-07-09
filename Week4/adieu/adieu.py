import inflect

p = inflect.engine()


def main():
    adieu()


def adieu():

    names = []

    while True:
        try:
            user_input = input()
            names.append(user_input)
            continue

        except EOFError:
            if len(names) != 1:
                names[-1] = "and " + names[-1]

            if len(names) == 2:
                print(f"\n Adieu, adieu, to {' '.join(names)}", end=".")
            else:
                print(f"\n Adieu, adieu, to {', '.join(names)}", end=".")

            break


if __name__ == "__main__":
    main()
