import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def wyszukaj(w):
    w = w.lower()
    if w in data.keys():
        return data[w]
    elif get_close_matches(w, data.keys()):
        user_input2 = input(f'czy chodzilo ci o {get_close_matches(w, data.keys())[0]} ? T/N')

        if user_input2 == 'T':
            return get_close_matches(w, data.keys())[0]
        elif user_input2 == 'N':
            return f'brak wartosci'
        else:
            return f'prosze podaj wartosc t/n '
        # return f'czy chodzilo ci o {get_close_matches(w, data.keys())[0]}'
    else:
        return f'wartosc dla {w} nie zostala znaleziona'

print(f'name: {data["name"]}')

user_input = input("podaj wyraz ")


print(f'wartosci to: {wyszukaj(user_input)}')

if type(wyszukaj(user_input)) == list:
    for item in wyszukaj(user_input):
        print(item)
else:
        print(wyszukaj(user_input))