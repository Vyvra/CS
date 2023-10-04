import requests
import sys

try:
    amount = float(sys.argv[1])
    if len(sys.argv) != 2:
        raise ReferenceError

except ReferenceError:
    print("please supply exactly one argument")
except:
    print("please specify amount as a float")
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    price = response.json()['bpi']["USD"]["rate_float"]
    total = price * amount
    print(f"${total:,.4f}") 
except requests.RequestException:
    print("something went wrong")
    
