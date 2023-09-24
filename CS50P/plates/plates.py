def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not str(s[0:1]).isalpha():
        return False
    elif not (2 <= len(s) <= 6):
        return False
    else:
        prev_c = ""
        for c in s:
            if not (c.isalpha() or c.isdigit()):
                return False
            if c.isalpha() and prev_c.isdigit():
                return False
            if c == "0" and prev_c.isalpha():
                return False
            else:
                prev_c = c
        return True    


main()

