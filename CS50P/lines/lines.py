import sys


def main():
    args = sys.argv[:1]
    if len(args) < 1:
        sys.exit("Too few command-line arguments")
    elif len(args) > 1:
        sys.exit("Too many arguments")
    else:
        print(lines(sys.argv[1]))


def lines(file):
    with open(str(file), 'r') as file:
        loc = 0
        for line in file:
            if line != "\n":
                loc += 1
    return loc


if __name__ == "__main__":
    main()
