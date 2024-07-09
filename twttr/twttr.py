def main():

    shorten()

def shorten(word):
    vowels = "aeiouAEIOU"
    output = "".join(c for c in word if c not in vowels)
    print(output)

    return output

if __name__ == "__main__":
    main()