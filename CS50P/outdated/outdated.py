def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        try:
            date = input("Date: ").strip()
            if str(date[0]).isdigit():
                day = date.split("/")[1]
                month = date.split("/")[0]
                year = date.split("/")[2]
            else:
                if not "," in date.split(" ")[1]:
                    raise ValueError
                month = date.split(" ")[0]
                day = str(date.split(" ")[1]).split(",")[0]
                year = date.split(" ")[2]
            if month in months:
                month = months.index(month.title())+1
            if int(month) < 10:
                month = f"0{month}"
            if int(day) < 10:
                day = f"0{day}" 
            if int(month) > 12:
                raise ValueError
            if int(day) > 31:
                raise ValueError
            if int(month) < 12:    
                print(f"{year}-{month}-{day}")
                break
        except:
            print("try again")


if __name__ == "__main__":
    main()  
