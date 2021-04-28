"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120"""

n = int(input('Entre com um numero para ser fatorado: '))

resultado = 1
count = 1

while count <= n:
    resultado *= count
    count += 1
print(resultado)
"""
numero = int(input('Entre com o numero: '))
resultado = 1
for n in range (1, numero + 1):
    resultado *= 
print(resultado)"""