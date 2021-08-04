"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""

print('Programa classificação criminal')
p1 = input('Telefonou para a vítima? (s/n): ')
p2 = input('Esteve no local do crime? (s/n): ')
p3 = input('Mora perto da vítima? (s/n): ')
p4 = input('Devia para a vitima? (s/n): ')
p5 = input('Já trabalhou com a vítima? (s/n): ')
lista = []
lista.append(p1)
lista.append(p2)
lista.append(p3)
lista.append(p4)
lista.append(p5)
count_s = 0
count_n = 0
for i in lista:
    if i == 's':
        count_s = count_s + 1
    else:
        count_n = count_n + 1

if count_s == 2:
    print('classificação = "suspeita"')
elif count_s == 3 or count_s == 4:
    print('classificação = "Cúmlice"')
elif count_s == 5:
    print('classificação = "Assassino"')
else:
    print('Inocente...')
