import sys
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) > 1:
        if len(sys.argv) == 2 or len(sys.argv) > 3: 
            sys.exit("please use correct number of arguments")
        elif sys.argv[2] not in fonts:
            sys.exit("Font not found")
        elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
            figlet.setFont(font=sys.argv[2])
        elif (sys.argv[1] != "-f" or sys.argv[1] != "--font"): 
            sys.exit("Wrong flag: use -f or --font to select font")
    s = input("Input: ")
    print(figlet.renderText(s))
if __name__ == "__main__":
    main()
