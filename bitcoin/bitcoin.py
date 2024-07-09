import requests
import json
import sys


def main():
    bitcoin_index()


def bitcoin_index():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        elif sys.argv[1].isalpha():
            sys.exit("Command-line argument is not a number")

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitcoin_data = response.json()

        USD_rate = bitcoin_data["bpi"]["USD"]["rate_float"] * float(sys.argv[1])
        print(f"${USD_rate:,.4f}")

    except requests.RequestException:
        print("Nu's bani cumetre.")



if __name__ == "__main__":
    main()