def main():
    coke_machine()


def coke_machine():
    amount_due = 50
    accepted_coins = [5, 10, 25]

    print(f"Amount Due: {amount_due}")

    while True:
        inserted = int(input("Insert coin: "))
        if inserted not in accepted_coins:
            print(f"{amount_due}")
            continue
        amount_due -= inserted
        if amount_due <= 0:
            break
        print(f"Amount Due: {amount_due}")

    if amount_due < 0:
        print(f"Change Due: {abs(amount_due)}")
    else:
        print("Change Due: 0")


if __name__ == "__main__":
    main()
