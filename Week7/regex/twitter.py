import re

url = input("What is your twitter url? ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url):
    print(f'Username: {matches.group(1)}')