from pyfiglet import Figlet
from random import choice
import sys


def main():
    figlet()


def figlet():

    figlet = Figlet()

    if len(sys.argv) == 1:
        user_input = input('Input: ')
        figlet.setFont(font=choice(figlet.getFonts()))
        print(f"Output:\n{figlet.renderText(user_input)}")


    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in figlet.getFonts():
        user_input = input('Input: ')
        figlet.setFont(font=sys.argv[2])
        print(f"Output:\n{figlet.renderText(user_input)}")

    else:
        sys.exit("Invalid usage")


main()