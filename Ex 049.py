"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores."""

soma = 0
condition = True
numero = []

while condition:
    n = int(input('Informe um numero: '))
    if n != 0:
        soma += n
        numero.append(n)
    else:
        break

print('Soma: ', soma)
print('Menor valor: ', min(numero))
print('Mairo valor: ', max(numero))