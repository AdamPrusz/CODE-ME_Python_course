# Ogrodnik. Utwórz program - udający poradnik ogrodnika. Powinien zawierać dowolny słownik
# przypominający o obowiązkach ogrodniczych w zależności od miesiąca. np. styczeń - bielenie pni drzew,
# październik - czas posadzić wiosenne krzewy. Użytkownik może podać skróconą, 3 literową nazwę
# miesiąca i otrzymać poradę. Użytkownik kończy korzystanie z programu naciśnięciem przycisku - Q.

garden = {
    'Styczeń': 'Rośliny podlewamy umiarkowanie i nie nawozimy ich.',
    'Luty': 'Tak samo jak w styczniu,Rośliny podlewamy umiarkowanie i nie nawozimy ich.',
    'Marzec': "marcowanie",
    'Kwiecień': "kwietniowanie",
    'Maj': 'majowanie',
    'Czerwiec': 'czerwcowanie',
    'Lipiec': 'lipcowanie',
    'Sierpień': 'sierpowanie',
    'Wrzesień:': 'wrzesniowanie',
    'Październik': 'październikowanie',
    'Listopad': 'listopadowe',
    'Grudzień': 'grudniowanie'
}

def get_months_list(dictionary):
    new_months = []
    for step in dictionary.keys():
        new_months.append(step)

    return new_months


def user_choice(list, dictionary):
    while len(list) > 0:
        user = input("Podaj nazwę miesiąca lub 3 pierwsze litery:  ")
        for step in list:
            if user[0:3] in step:
                to_do = dictionary[step]
                print(to_do)








months = get_months_list(garden)
user_choice(months,garden)




