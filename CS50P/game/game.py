import random
def main():
    n = ""
    while n == "":
        inputn = input("Level: ")
        if str(inputn).isdigit():
            inputn = int(inputn)
            if 0 < int(inputn) < 100:
                n = inputn
            else:
                print("out-of-range")
    x = random.randint(1, int(n))
    guess = ""
    while guess != x:
        guess = (input("Guess: "))
        if guess.isdigit() == True:
            guess = int(guess)
            if guess > n:
                print("Please enter number smaller than level")
            elif guess == x:
                print("Just right!")
            elif guess < x:
                print("Too small!")
            elif guess > x:
                print("Too large!")

if __name__ == "__main__":
    main()
