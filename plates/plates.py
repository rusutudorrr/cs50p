def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check minimum and maximum lenght
    if len(s) not in range(2,7):
        return False

    # All vanity plates must start with at least two letters.

    if not s[:2].isalpha():
        return False

    # Check that the first number is not 0
    string_nums = ['0','1','2','3','4','5','6','7','8','9']
    nums_in_string = []
    for c in s:
        if c in string_nums:
            nums_in_string.append(c)

    if len(nums_in_string) != 0:
        if nums_in_string[0] == "0":
            return False

    # Check that the last character is not a number

    if s[-1].isalpha() and s[-2].isdigit():
        return False

    if s[-1].isdigit() and s[-2].isalpha():
        return False

    # Check that there are no spaces, punctuation etc

    for c in s:
        if not c.isalnum():
            return False

    return True


main()
