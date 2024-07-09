import datetime
import sys
import inflect


def main():
    seasons_of_love()


def seasons_of_love():
    try:
        user_inp = input("Date of Birth: ")

        # get birthday from user input
        birthdate = datetime.datetime.strptime(user_inp, "%Y-%m-%d").date()
        today = datetime.date.today()

        # calculate the difference in days
        days_difference = (today - birthdate).days
        minutes = days_difference * 24 * 60  #convert days to minutes

        # convert minutes to words and format to pass all checks
        minutes_in_words = inflect.engine().number_to_words(minutes).replace(" and", "").capitalize()

        print(f"{minutes_in_words} minutes")
        return minutes

    except ValueError:
        sys.exit("Invalid date")


def is_leap_year(year):
    """ Check if a year is a leap year """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def count_leap_years(start, end):
    """ Count the number of leap years between two dates, considering the dates as well """
    leap_years = 0
    for year in range(start.year, end.year + 1):
        if is_leap_year(year):
            feb29 = datetime.date(year, 2, 29)
            # check for feb29th in the leap year
            if start <= feb29 <= end:
                leap_years += 1
    return leap_years


if __name__ == "__main__":
    main()
