password = input("podaj haslo:")

length_correct = password >= 8
includes_letters_and_digits = password.isalnum() and not password.isdigit()and not password.isalpha()
at_lest_one_captal_letter = not password.islower()

if not length_correct:
    print("haslo jest za krotkie, haslo mu miec min. 8 znakow")

if not includes_letters_and_digits:
    print("haslo powinnno skladac sie z liter i cyfr")

if not at_lest_one_captal_letter:
    print("Musi zawierać co najmniej 1 literę")


