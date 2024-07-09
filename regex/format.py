import re

name = input("What is your name? ").strip()

if matches := re.search(r"^(.+), *(.+)$", name):
    name = f"{matches.group(2)} {matches.group(1)}"
print(f"Hello, {name}")