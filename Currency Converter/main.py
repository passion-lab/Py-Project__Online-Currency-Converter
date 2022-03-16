import requests
from json import loads


timeout = 5
url = "https://currency-converter-by-api-ninjas.p.rapidapi.com/v1/convertcurrency"
querystring = {"have": "USD", "want": "INR", "amount": 5.2}
headers = {
    'x-rapidapi-host': "currency-converter-by-api-ninjas.p.rapidapi.com",
    'x-rapidapi-key': "babadbf43cmsh60ba150f564e3b2p1d73b5jsn7ecb33142b43"
}

# print("It's an internet based application. Please hold on while we connect.")
# print("Connecting to internet...")
# try:
#     requests.get(url=url)
#     print("Connected to the Internet!\n")
# except (ConnectionError, requests.Timeout) as exception:
#     print("No internet connection.\nPlease connect to the internet and try again.")

with open("countries.txt") as file:
    data = file.read().split("\n")
    countries = {}
    countries.update({item[:3]: item[3:].strip("\t") for item in data})


while True:
    print("Give any currency code in three digits format (e.g., USD) only.\n"
          "Type 'M' for available currencies and 'Q' to Quit.\n")
    _from = input("   _From: ").strip().upper()

    if _from in countries:
        while 1:
            _to = input("     _To: ").strip().upper()
            if _to in countries:
                querystring['have'] = _from
                querystring['want'] = _to
                while 1:
                    _val = input(f" _Amount: ").strip()
                    try:
                        querystring['amount'] = float(_val)
                        break
                    except ValueError:
                        print(" WRONG: Not a valid input!"
                              " Please type only available number corresponding to each country.")
                        continue
                break
            elif _to == 'Q':
                exit()
            else:
                print(" WRONG: You have to enter a valid currency code like before.\n")
                continue
        break

    elif _from == 'M':
        print("\nCurrency Codes: ")
        for key, _ in countries.items():
            print(key, end=" | ")
        print("\n")
        continue

    elif _from == 'Q':
        exit()

    else:
        print(" WRONG: You have to enter a valid currency code.\n")

response = loads(requests.get(url, headers=headers, params=querystring).text)
print(f"\n > {response['old_amount']} {response['old_currency']} = {response['new_amount']} {response['new_currency']}")
