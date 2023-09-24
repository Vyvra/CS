def main():
    due = 50
    coins = 0
    while coins < due:
        print(f"Amount Due: {due}" )
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            due = due - coin

    if coins >= due:
        print(f"Change Owed: {coins-due}" )
if __name__ == "__main__":
    main()
