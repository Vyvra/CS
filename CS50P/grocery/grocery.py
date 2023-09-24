def main():
    groceries = []
    while True:
        try:
            item = input("")
            groceries.append(item)
        except EOFError:
            groceries.sort()
            printed = []
            for item in groceries:
                if item not in printed:
                    print(f"{groceries.count(item)} {str(item).upper()}")
                    printed.append(item)
            break
if __name__ == "__main__":
    main()    
