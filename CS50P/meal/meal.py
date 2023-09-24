def main():
    time = input("What time is it?")
    floattime = convert(time)


    if floattime >= 7 and floattime <= 8:
        print("breakfast time")
    elif floattime >= 18 and floattime <= 19:
        print("dinner time")
    elif floattime >= 12 and floattime <= 13:
        print("lunch time")

def convert(time):
    hour = time.split(":")[0]
    minutes = time.split(":")[1]
    floattime = float(hour) + (float(minutes) / 60) 
    return floattime    

if __name__ == "__main__":
    main()   
        



