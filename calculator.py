def main():
    x = input("What's x? ")
    print(f"x squared is {square(x)}")

def square(n):
    return n * n

if __name__ == "__main__":
    main()