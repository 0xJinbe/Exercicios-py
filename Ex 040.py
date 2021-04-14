"""Faça um programa que leia 5 números e informe o maior número."""

#com while
maior = -99
i = 1
while i <= 5:
    wnumero = int(input('Informe um numero: '))
    if wnumero > maior:
        maior = wnumero
    i += 1
print(maior)

#com for

mairo = -99
for i in range (5):
    fnumero = int(input('Informe um numero: '))
    if fnumero > mairo:
        mairo = fnumero
print(mairo)