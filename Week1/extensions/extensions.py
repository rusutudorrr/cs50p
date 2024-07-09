def main():
    file_extension()


def file_extension():
    user_input = input("File name: ").strip()

    if "." in user_input:
        extension = user_input.split(".")[-1]
    else:
        extension = user_input

    match extension:
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "gif":
            print("image/gif")
        case "png":
            print("image/png")
        case "pdf" | "PDF":
            print("application/pdf")
        case "zip":
            print("application/zip")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")


if __name__ == "__main__":
    main()
