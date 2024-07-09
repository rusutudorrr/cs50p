import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^([0-9]{1,3}\.)([0-9]{1,3}\.)([0-9]{1,3}\.)([0-9]{1,3})$"
    if matches := re.search(pattern, ip):
        octets = matches.groups()
        for octet in octets:
            cleaned_octet = int(octet.strip('.'))
            if not (0 <= cleaned_octet <= 255):
                return False
            return True
    else:
        return False


if __name__ == "__main__":
    main()
