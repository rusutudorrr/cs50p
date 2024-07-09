import emoji

def main():
    emojize()

def emojize():

    user_input = input("Input: ")
    output = emoji.emojize(user_input, language="alias")
    print(f"Output: {output}")

main()