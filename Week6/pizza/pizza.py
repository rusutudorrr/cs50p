import sys
from tabulate import tabulate


def main():
    pizza()


def pizza():
    if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
        try:
            rows = []
            with open(sys.argv[1], 'r') as file:
                for line in file:
                    if not line.isspace():
                        rows.append(line.rstrip().split(','))
                headers, table = rows[0], rows[1:]
                print(tabulate(table, headers, tablefmt='grid'))

        except FileNotFoundError:
            sys.exit("File does not exist")
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    else:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
