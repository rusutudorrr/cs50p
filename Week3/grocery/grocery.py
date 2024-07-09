def main():
    grocery_list()


def grocery_list():

    groceries = {}

    while True:
        try:
            user_input = input()
            if user_input in groceries:
                groceries[user_input] += 1
            else:
                groceries[user_input] = 1
            continue

        except EOFError:
            for grocery, count in sorted(groceries.items()):
                print(f'{count} {grocery.upper()}')
            break


main()
