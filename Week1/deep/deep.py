def the_meaning_of_life():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

    match user_input:
        case '42' | 'forty-two' | 'forty two':
            print("Yes")
        case _:
            print("No")


the_meaning_of_life()
