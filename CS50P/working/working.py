import re
from typing import _ProtocolMeta

def main():
    print(convert(input("Hours: ")))


def convert(s):
    #time = re.search(r"(\d{1,2}(?::\d\d\)? (?:AM|PM) to (\d{1,2}(?::\d\d\)? (?:(AM)|(PM)) )", s)
    time = re.findall(r"\d{1,2}(?::\d{2})?", s)
    ampm = re.findall(r"(?:A|P)M", s)
    print(time, ampm)
    if not time:
        raise ValueError 
    if int(time[0][0:1]) > 12 or int(time[1][0:1]) > 12:
        raise ValueError
    convertedtime = ""
    if ampm[0] == "PM":
        ampm[0] == 12
    else:
        ampm[0] == 0
    
    convertedtime = time[]



if __name__ == "__main__":
    main()
