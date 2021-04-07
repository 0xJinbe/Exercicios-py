"""Faça um Programa que leia três números e mostre o maior deles.
"""

num_1 = float(input('Entre com o primeiro numero: '))
num_2 = float(input('Entre com o segundo numero: '))
num_3 = float(input('Entre com o terceiro numero: '))

if num_1 > num_2 and num_1 > num_3:
    print('O primeiro numero é o maior', num_1)
elif num_2 > num_1 and num_2 > num_3:
    print('O segundo numero e o maior ', num_2)
elif num_3 > num_1 and num_3 > num_2:
    print('O terceiro numero é o maior.', num_3)


