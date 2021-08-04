"""Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

num_1 = float(input('Entre o primeiro numero: '))
num_2 = float(input('Entre com o segundo numero: '))
num_3 = float(input('Entre com o terceiro numero: '))

menor = 0
maior = 0
if num_1 > num_2 and num_1 > num_3:
    maior = num_1
elif num_2 > num_1 and num_2 > num_3:
    maior = num_2
elif num_3 > num_1 and num_3 > num_2:
    maior = num_3
print('O maior numero é: ', maior)

if num_1 < num_2 and num_1 < num_3:
    menor = num_1
elif num_2 < num_1 and num_2 < num_3:
    menor = num_2
elif num_3 < num_1 and num_3 < num_2:
    menor = num_3
print('O menor numero é: ', menor)
