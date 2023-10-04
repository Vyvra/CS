from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("Welcome to Twitter") == "Wlcm t Twttr"
    assert shorten("HI!, nr. 1") == "H!, nr. 1"

if __name__ == "__main__":
    main() 
