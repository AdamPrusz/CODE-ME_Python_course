#Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.

password = input('Podaj hasło:')
if len(password) < 8:
    print('Hasło ma za mało znaków')

if password.islower():
    print('Hasło musi zawierać co najmniej jedną dużą litertę.')



if password.isalpha():
    print('Hasło musi zawierać cyfry.')

elif password.isdigit():
    print('Hasło musi zawierać litery')

elif not password.isalnum():
    print('Hasło nie może zawierać spacji ani znaków specjalnych')
