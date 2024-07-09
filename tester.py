import sys


def main():
    word = argument_getter()
    print(string_reversal(word))


def string_reversal(word: str) -> str:

    reversed_letters = []

    try:
        for letter in word:
            reversed_letters.insert(0, letter)
        reversed_string = "".join(reversed_letters)
        return reversed_string

    except TypeError:
        print("Must type a word.")


def argument_getter():

    try:
        if sys.argv[1].isalpha():
            return sys.argv[1]

    except IndexError:
        print("Must type a word.")


if __name__ == "__main__":
    main()

