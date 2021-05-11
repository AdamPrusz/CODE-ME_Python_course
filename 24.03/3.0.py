filename = 'Pantadeusz.txt'

with open(filename, 'r',encoding='utf-8') as file:
    content = file.readlines()

print('----------------------------')

# for index in range(len(content)):
#     print(f"{index} -> {content[index]}")

#lub

for index, line in enumerate(content):
    print(index, '-->', line)
