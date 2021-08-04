"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."""

print('Entre com o preço dos 3 produtos que deseja comprar')

p1= float(input('Preço 1: '))
p2 = float(input('Preço 2: '))
p3 = float(input('Preço 3: '))

mais_barato = 0
if p1 < p2 and p1 < p3:
    mais_barato = p1
if p2 < p1 and p2 < p3:
    mais_barato = p2
if p3 < p1 and p3 < p2:
    mais_barato = p3
print('O mais barato é: ', mais_barato)