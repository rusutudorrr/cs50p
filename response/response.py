import validators


def main():
    print(validate_email(input("What's your email address:? ")))


def validate_email(user_input):
    return "Valid" if validators.email(user_input.strip()) == True else "Invalid"


if __name__ == "__main__":
    main()