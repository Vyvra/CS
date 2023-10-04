import working


def main():
    print(working.convert("9:00 AM to 5:00 PM"))

def test_convert():
    assert working.convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
if __name__ == "__main__":
    main()
