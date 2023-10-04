import plates

def test_is_valid():
    platesdict = {
        "CS50" : True,
        "CS05" :False,
        "CS50P": False,
        "PI3.14" : False,
        "H" : False,
        "OUTATIME" : False,
        "13.14" : False,
    }
    for key in platesdict:
        print(f"Checking if {key} results in response {platesdict[key]}")
        assert plates.is_valid(key) == platesdict[key]

if __name__ == "__main__":
    test_is_valid()
