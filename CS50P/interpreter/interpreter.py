def main():
    e = input("Expression: ").split(" ")
    match e[1]:
        case "+":
            print(float(e[0]) + float(e[2]))

        case "*":
            print(float(e[0]) * float(e[2]))

        case "-":
            print(float(e[0]) - float(e[2]))

        case "/":
            print(float(e[0]) / float(e[2]))
if __name__ == "__main__":
    main()         
