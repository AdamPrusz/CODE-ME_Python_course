# Wywołaj błąd związany z otwarciem pliku. Spróbuj odczytać plik, który nie istnieje. Spróbuj odczytać wartość
# z pliku otwartym w trybie w. Spróbuj utworzyć plik, który już istnieje w trybie x. Obsłuż w dowolny sposób każdy
# z powyższych błędów.

def open_file(file, method):

    filename = file + '.txt'
    if method == 'w':
        content = "'W' method is used only for writing. Try to use different method. "
    else:
        try:
            with open(filename, user_method) as fp:
             content = fp.readlines()
        except FileExistsError:
            content = f"The file {filename} already exists!. Try again"
        except FileNotFoundError:
            content = f"The file {filename} do not exists. Try again"
        except ValueError:
            content ="Something went wrong. Try again"

    return content

if __name__ == "__main__":
    user_file = input("Gimme file name: ")
    user_method = input("Gimme method: ")
    print(open_file(user_file, user_method))





