def faces():
    user_input = input()

    if user_input == "Hello :)":
        print("Hello 🙂")
    elif user_input == "Goodbye :(":
        print("Goodbye 🙁")
    elif user_input == "Hello :) Goodbye :(":
        print("Hello 🙂 Goodbye 🙁")
    else:
        print(user_input)


faces()