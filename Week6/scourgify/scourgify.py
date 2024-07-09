import sys


def main():
    scourgify()


def scourgify():

    if len(sys.argv) == 3 and sys.argv[1].endswith('.csv'):

        try:
            with open(sys.argv[1], 'r') as file:
                # Skip the header line
                next(file)

            with open(sys.argv[2], 'w') as op:
                # Write header to the output
                op.write("first,last,house\n")

                for line in file:
                    cleaned_line = line.replace('"', '').strip()
                    data = cleaned_line.split(',')

                    last, first, house = data[0].strip(), data[1].strip(), data[2].strip()

                    op.write(f"{first},{last},{house}\n")

        except FileNotFoundError:
            sys.exit(f'Could not read {sys.argv[1]}')

    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')


if __name__ == "__main__":
    main()
