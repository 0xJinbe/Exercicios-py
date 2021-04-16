"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

f=lambda x :x if x<=2 else x*f(x-1)

print(f(5))