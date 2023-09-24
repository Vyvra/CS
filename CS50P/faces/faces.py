def main():
    text = input("What? \n")
    convert(text)

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    print(text)

if __name__ == "__main__":
    main()
