"""Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

n1 = float(input('Entre n1: '))
n2 = float(input('Entre n2: '))
n3 = float(input('Entre nc: '))

lista = []
lista.append(n1)
lista.append(n2)
lista.append(n3)
lista_decrescente = sorted(lista, reverse=True)
print(lista_decrescente)

#também funciona

lista_com_for = []
qnt = 3
for i in range(qnt):
    elemento = int(input('Digite um numero: '))
    lista_com_for.append(elemento)
lista_com_for.sort(reverse=True)
print(lista_com_for)
