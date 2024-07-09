def greeting():
    user_input = input("Greeting: ")

    match user_input:
        case "Hello" | " Hello " | "Hello, Newman":
            print("$0")
        case "How you doing?":
            print("$20")
        case "What's happening?" | _:
            print("$100")


greeting()