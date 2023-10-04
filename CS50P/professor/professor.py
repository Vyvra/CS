import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = ""
        errors = 0
        while answer != (x + y):
            guess = input(f"{x} + {y} = ")
            if guess.isdigit():
                answer = int(guess)
                if answer != (x + y):
                    print("EEE")
                    errors = errors + 1
                    if errors == 3:
                        input(f"{x} + {y} = {x+y}")
                        break
                else:
                    score = score + 1
    print(f"Score: {score}")


def get_level():
    while True:
        s = input("Level: ")
        if s.isdigit():
            s = int(s)
            if s == 1 or s == 2 or s == 3:
                return s


def generate_integer(level):
    if level != 1 and level != 2 and level != 3:
        raise ValueError
    if level == 1:
        return random.randint((10 ** (level - 1) - 1), (10 ** (level) - 1))
    else:
        return random.randint((10 ** (level - 1) - 1), (10 ** (level) - 1)) + 1


if __name__ == "__main__":
    main()
