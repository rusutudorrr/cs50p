def main():
    word = 'Twitter'
    print(shorten(word))


def shorten(word):
    vowels = "aeiouAEIOU"
    output = "".join(c for c in word if c not in vowels)

    return output


if __name__ == "__main__":
    main()
