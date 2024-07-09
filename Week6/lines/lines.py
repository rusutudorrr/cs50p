import sys


def main():
    count_lines()


def count_lines():
    if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
        try:
            with open(sys.argv[1], 'r') as file:
                counter = 0
                for line in file:
                    if line.lstrip().startswith("#") or line.isspace():
                        continue
                    counter += 1
                print(counter, end='')
        except FileNotFoundError:
            sys.exit('File does not exist')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        sys.exit("Not a Python file")


if __name__ == '__main__':
    main()
    