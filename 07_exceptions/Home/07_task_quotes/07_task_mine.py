# 7▹ Wróć do pierwszego zadania z lekcji o plikach, zmodyfikuj go tak, aby to użytkownik podawał nazwę pliku z cytatami.
# Pamiętaj, by użytkownik po wykonaniu błędnej akcji (np. literówki w nazwie pliku) miał możliwość poprawić swój błąd.

import quotes_module as qm

def user_quoute():
        while True:
                user_name = input("Gimme the name of file: ")
                filename = user_name + ".txt"
                try:
                        with open(filename, 'r', encoding='utf-8') as fopen:
                                content = fopen.readlines()
                        break
                except FileNotFoundError:
                        print("File not found. Try again")
                        continue
        return content


if __name__ == "__main__":
        quote = qm.select_quote(user_quoute())
        quote = qm.reformat(quote)
        qm.show(quote)
