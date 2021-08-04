"""Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
"""


num = int(input("Digite um numero: "))
lista = []
if num < 2: # 0 e 1 não são primos, e vou desconsiderar os números negativos
    print('não é primo')
elif num == 2: # 2 é o único número par que é primo
    print('primo')
elif num % 2 == 0: # se for par e não é 2, não é primo
    print('não é primo')
    for i in range(1,num+1):
        if num % i == 0:
            lista.append(i)
    print(f'Os n° {num} é divisível por {lista}')
else: # aqui eu sei que o número é ímpar # só testo se é divisível por números ímpares
    for i in range(1, num + 1, 2):
        if num % i == 0:
            lista.append(i)
            print('não é primo')
            print(lista)
            break # não é primo, interrompe o for
        print(f'Os n° {num} é divisível por {lista}')
    else:
            print('é primo')