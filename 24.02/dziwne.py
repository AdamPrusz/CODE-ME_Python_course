text = input ("wpisz dowolne znaki: ")
text_l = len(text)
new_text = ""
for step in range(text_l):
    #new_text = new_text + step
    if (step+2) % 2 == 0:
        print(text[step], end='')

