from bank import value
import sys

def main():
    test_value()


def test_value():
    assert value("Hello") == "$0"
    assert value("How are you!") == "$20"
    assert value("What's up!") == "$100"
    assert value("hello") == "$0"

if __name__ == "__main__":
    main()
