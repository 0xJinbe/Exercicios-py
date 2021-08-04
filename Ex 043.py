"""Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""

n1 = int(input('Escreva n1: '))
n2 = int(input('Escreva n2: '))

for i in range(n1, n2, 1):
    print(i)

#Altere o programa anterior para mostrar no final a soma dos números.

inicio = int(input("digite o inicio do intervalo-->"))
fim = int(input("digite o fim do intervalo-->"))
lista = []
for i in range (inicio, fim, 1):
    lista.append(i)
    s = sum(lista)
print(s)