import datetime


def main():

    while True:
        try:
            date = get_date()
            print(date.strftime("%Y-%m-%d"))
            break
        except ValueError:
            print("Date not valid")


def get_date():

    MONTHS = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    date_str = input("Date: ").strip()

    try:
        date = datetime.datetime.strptime(date_str, "%m/%d/%Y")
        return date
    except ValueError:
        print("Date not valid")

    try:
        month = date_str.split(" ")[0]
        day = int(date_str.split(",")[0].split(" ")[1])
        year = int(date_str.split(",")[1])

        if month not in MONTHS:
            raise ValueError("Month not found")

        date = datetime.datetime(year, MONTHS.index(month) + 1, day)
        return date
    except (ValueError, IndexError):
        raise ValueError("Date not valid")


main()
