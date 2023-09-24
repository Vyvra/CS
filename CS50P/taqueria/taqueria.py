def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    } 
    cost = 0
    while True:
        try:
            item = input("Item: ")
            cost = cost + menu[item.title()]
            print(f"Total: ${format(cost, '.2f')}")
        except EOFError:
            print("Thank you!")
            break
        except:
            print("Please try again")



if __name__ == "__main__":
    main()
