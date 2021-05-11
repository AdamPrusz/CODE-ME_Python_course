# Utwórz dekorator @uppercase_decorator, który przyjmuje dowolną funkcję zawracającą łańcuch
# znaków i zwracający ten sam tekst zmieniony na wielkie litery.
#
# Utwórz funkcję zwracającą tekst
#
# Utwórz dekorator przyjujący tę funkcję
#
# Wywołaj funkcję, by sprawdzić, że decorator działa

def uppercase_decorator(parametr):

    def read_text(): # funckja lokalna
        print(parametr.upper())

    return read_text()

word = uppercase_decorator()

