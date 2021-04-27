"""Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um."""

cds = int(input('Qual a quantidade de cds da coleção? '))
list = []

for i in range(cds):
    vlr = int(input('Qual o valor de cada cd? '))
    list.append(vlr)
print(f"A media do valor gasto por cd na coleção é de: {(sum(list)/len(list))}")