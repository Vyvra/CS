import inflect

p = inflect.engine()


def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            adieu = p.join(names)
            print(f"Adieu, adieu, to {adieu}")
            break


if __name__ == "__main__":
    main()
