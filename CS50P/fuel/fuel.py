def main():
    while True:
        f = input('Fraction: ')
        try:
            numerator = int(f.split("/")[0])
            denomenator = int(f.split("/")[1])
            if denomenator == 0:
                print("Please don't divide by zero")
            elif numerator / denomenator > 1:
                print("More than 100%")
            elif numerator / denomenator >= 0.99:
                print('F')
                break
            elif numerator / denomenator <= 0.02:
                print('E')
                break
            else:
                print(f"{round((numerator / denomenator) * 100)}%")
                break
        except ValueError:
            print("Please supply fuel as a fraction of the form X/Y")
main()        
