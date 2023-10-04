import emoji


def main():
    text_to_emojize = input("Input: ")
    print(emoji.emojize(f"{text_to_emojize}", language="alias"))


if __name__ == "__main__":
    main()
