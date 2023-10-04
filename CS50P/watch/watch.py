import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = re.findall(r"<iframe.*https?://(?:www\.)?youtube\.com/embed/(.{11})", s)
    if s:
        return (f"https://youtu.be/{s[-1]}")


if __name__ == "__main__":
    main()

