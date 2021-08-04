"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

n = int(input('Entre com um numero para a sequencia Fibonacci: '))

lista = []
u1 = 1
u2 = 1
count = 0
for i in range (0, n):
    count = u1 + u2
    u1 = count
    u2 = count - u2
    lista.append(count)
print(lista)

