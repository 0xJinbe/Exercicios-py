"""Faça um programa que calcule o mostre a média aritmética de N notas."""

n = int(input('Digite a quantidade de notas que deseja calcular: '))
count = 0
l = []

while count < n:
    l.append(float(input('Digite o valor da nota: ')))
    count += 1

print(f"A média de todas as notas é: {sum(l)/len(l)}")


"""n = float(input('Entre com as notas a serem calculadas: '))
l = []

while n > 0:
    n = float(input('Entre com as notas a serem calculadas: '))
    l.append(n)

print(f"A medias das notas é: {sum(l)/len(l)}")"""

