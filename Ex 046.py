"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""

lista_par = []
lista_impar = []
count_par = 0
count_impar = 0
for i in range (10):
    n = int(input('Entre com os numeros: '))
    if n % 2 == 0:
        count_par += 1
        lista_par.append(n)
    elif n % 2 != 0:
        count_impar += 1
        lista_impar.append(n)
print(f"Lista impar: {lista_impar} quantidade impar: {count_impar}, lista par: {lista_par}, quantidade par: {count_par}")

