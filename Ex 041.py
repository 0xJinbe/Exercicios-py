"""Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
lista = []
i = 1
while i <= 5:
    a = int(input('Informe os numeros: '))
    lista.append(a)
    media = sum(lista)/len(lista)
    soma = sum(lista)
    i += 1
print(lista, soma, media)

l = []
for i in range (5):
    a = int(input('Informe os valores: '))
    l.append(a)
    m = sum(l)/len(l)
    s = sum(l)
print(l, s, m)