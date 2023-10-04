import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
# four sets of 0-255
    matches = re.search(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3}$)", ip)
    if not matches or 3 > len(matches.groups()) > 4:
        return False
    else:    
        for i in range(len(matches.groups())):
            if int(matches.group(i+1)) > 255:
                return False    
        return True


if __name__ == "__main__":
    main()
