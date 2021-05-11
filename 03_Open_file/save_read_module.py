# Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje bezpieczny sposób odczytu oraz
# bezpieczny zapis. Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty.
# Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.

import os

def open_the_file(filename):
    filename = filename + ".txt"
    if os.path.exists(filename) is True and os.path.getsize(filename) != 0:
        with open (filename) as f:
            content = f.readlines()
            print(content)
    elif os.path.exists(filename) is False:
        print("The file does not exists!")
    else:
        print("The file is empty!")

def save_the_file(filename):
    filename = filename + ".txt"
    f = open(filename, "a")
    f.close()



