def main():
    camel_to_snake()


def camel_to_snake():
    user_input = input("camelCase: ")

    snake_case = ""
    i = 0
    while i < len(user_input):
        letter = user_input[i]
        if i > 0 and letter.isupper() and user_input[i-1].islower():
            snake_case += "_"
        snake_case += letter.lower()
        i += 1
    print(f"snake_case: {snake_case}")
    return snake_case


if __name__ == "__main__":
    main()
