"""Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada."""

n = int(input('Quantas pessoas participarão da turma? '))
count = 0
l = []

while count < n:
    count += 1
    l.append(int(input('Qual a idade a ser calculada? ')))

media = sum(l)/len(l)
if 0 < media and media < 25:
    print(f"A media da turma é {media}. A turma se classifica como JOVEM")
elif media > 26 and media < 60:
    print(f"A media da turma é {media}. A turma se classifica como ADULTA")
else:
    print(f"A media da turma é {media}. A turma se classifica como IDOSA")