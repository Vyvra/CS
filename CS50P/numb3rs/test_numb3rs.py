import pytest
import numb3rs

def main():
    test_validate()

def test_validate():
    assert numb3rs.validate("123.123.123.123") == True
    assert numb3rs.validate("255.255.280.25") == False
    assert numb3rs.validate("abc.123.123.123") == False
    assert numb3rs.validate("0.0.0.1234") == False
if __name__ == "__main__":
    main()
