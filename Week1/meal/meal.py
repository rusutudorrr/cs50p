def main():
    user_input = input("What time is it? ")

    time = convert(user_input)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        pass


def convert(time):
    hours, minutes = time.split(":")
    time = int(hours) + int(minutes) / 60
    return time


if __name__ == "__main__":
    main()
