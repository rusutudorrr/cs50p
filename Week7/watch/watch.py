import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'<iframe.*?src="(https?://)(?:www\.)?(youtube)\.com/embed(/\w*)".*?>.*?</iframe>'
    if match := re.search(pattern, s.strip()):
        yt = match.group(2).replace('youtube', 'youtu.be')
        link = match.group(3)
        return f'https://{yt}{link}'


if __name__ == "__main__":
    main()
