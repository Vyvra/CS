def main():
    g = input("Greeting: ").lower().strip()
    if g[0:5] == "hello":
        print("$0")
    elif g[0] == "h":
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
     main()
