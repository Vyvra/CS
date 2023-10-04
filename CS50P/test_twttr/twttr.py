def main():
    long_word = input("Input: ")
    print(f"Output: {shorten(long_word)}")

def shorten(word):
    shrt_wrd = []
    for c in word:
        vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
        if c not in vowels:
            shrt_wrd.append(c)
    return "".join(shrt_wrd)


if __name__ == "__main__":
    main()
