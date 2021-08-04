"""A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
"""

lista = []
u1 = 1
u2 = 1
count = 0
for i in range (0, 13):
    count = u1 + u2
    u1 = count
    u2 = count - u2
    lista.append(count)
    #if count > 500:
print(lista)
