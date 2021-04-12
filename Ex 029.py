"""Faça um programa que peça um numero e informe se ele é inteiro ou decimal. Utilize função de arredondamento"""

num = float(input('Digite um numero: '))

if num == round(num):
    print('Número inteiro...')
else:
    print('Decimal ')
    print('Arredondando para baixo: ', round(num-0.5))
    print('Arredondando para cima: ', round(num+0.5))