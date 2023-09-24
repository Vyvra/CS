def main():
    t = list(input("camelCase: "))
    s = []
    for i in t:
        if i.lower() == i:
            s.append(i)
        else:
            s.append("_")
            s.append(i.lower())
    print(f"snake_case: {''.join(s)}")
if __name__ == "__main__":
    main()
