def main ():
    nutrition()


def nutrition():

    user_input = input("Item: ").lower()

    calories = {
        "apple": 130,
        "avocado": 50,
        "sweet cherries": 100,
        "kiwifruit": 90,
        "pear": 100
        }

    if user_input in calories:
        print(f"Calories: {calories[user_input]}")


main()