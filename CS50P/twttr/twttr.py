def main():
    s = input("Input: ")
    for c in s:
        vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
        if c not in vowels:
            print(c, end="")
    print("")
if __name__ == "__main__":
    main()
