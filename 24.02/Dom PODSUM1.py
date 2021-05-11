#1▹ Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych
# przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.

choose_names = input ("wpisz dowony ciag imion, rozdzielony przecinkiem lub spacja: ")

names_space = choose_names.replace(" ", ",")

names = names_space.split(",")


for step in names:
    print ("Hello", step)




