import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    # 
    pattern = re.compile(r'(\d{1,2})(?::(\d{2}))?\s{1}(AM|PM)?\s*to\s*(\d{1,2})(?::(\d{2}))?\s{1}(AM|PM)?')

    match = pattern.match(s)
    if not match:
        raise ValueError("Invalid time format")

    # unpack groups
    start_hour, start_minute, start_ampm, end_hour, end_minute, end_ampm = match.groups()
    # typecast values
    start_hour = int(start_hour)
    start_minute = int(start_minute) if start_minute is not None else 0
    end_hour = int(end_hour)
    end_minute = int(end_minute) if end_minute is not None else 0

    # validate time components
    if not (1 <= start_hour <= 12) or not (0 <= start_minute < 60) or not (1 <= end_hour <= 12) or not (0 <= end_minute < 60):
        raise ValueError("Invalid time")

    # Handle 12 AM and 12 PM specifically
    if start_hour == 12:
        start_hour = 0 if start_ampm == 'AM' else 12
    elif start_ampm == 'PM':
        start_hour += 12

    if end_hour == 12:
        end_hour = 0 if end_ampm == 'AM' else 12
    elif end_ampm == 'PM':
        end_hour += 12

    # format time strings in 24-hour format with two digits
    start_time_24 = f'{start_hour:02d}:{start_minute:02d}'
    end_time_24 = f'{end_hour:02d}:{end_minute:02d}'

    return f'{start_time_24} to {end_time_24}'


if __name__ == "__main__":
    main()
