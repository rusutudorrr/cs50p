def main():
    taqueria("Item: ")


def taqueria(prompt: str):

    items = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }

    total = 0
    while True:
        try:
            user_input = input(prompt).title()
            if user_input in items:
                total += items[user_input]
                print(f"Total: ${total:.2f}")
                continue
        except EOFError:
            print(f"Total: ${total:.2f}")
            print("\n")
            break


main()
