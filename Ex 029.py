"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal."""

#considerando operações como ações a serem escolhidas
"""
n1 = float(input('Qual o numero um? '))
n2 = float(input('Qual o numero dois? '))

op = input('Qual operação você deseja realizar? (1)par ou impar (2) positivo ou negativo (3) inteiro ou decimal')

if op == '1':
    if n1 % 2 == 0 and n2 % 2 == 0:
        print('Numero par')
    elif n1 % 2 != 0 and n2 % 2 != 0:
        print("Numero impar")
    elif n1 % 2 == 0 and n2 % 2 != 0:
        print(n1, 'É par...', n2, 'É impar')
    elif n1 % 2 != 0 and n2 % 2 == 0:
        print(n1, 'É impar', n2, 'É par')

else:
    pass

if op == '2':
    if n1 >= 0 and n2 >=0:
        print('Numeros positivos')
    elif n1 <= 0 and n2 <= 0:
        print('Numeros negativos.')
    elif n1 >= 0 and n2 <= 0:
        print(n1, 'é positivo', n2, 'É negativo')
    elif n1 < 0 and n2 >= 0:
        print(n1, 'é negativo', n2, 'é positivo')
else:
    pass

if op == '3':
    if round(n1) == n1 and round(n2) == n2:
        print('numeros integer')
    elif round(n1) == n1 and round(n2) != n2:
        print(n1, 'é integer', n2, 'e um numero float')
    elif round(n1) != n1 and round(n2) == n2:
        print(n1, 'é um numero float', n2, 'é um numero integer')
    else:
        print('numeros float')"""


#especie de calculadora, considerando operações como operações matematicas
num1 = input('Digite o primeiro numero: ')
num2 = input('Digite o segundo numero: ')

operação = input('Qual operação voce deseja: (+, -, *, /:')

if operação == '+':
    resultado = float(num1) + float(num2)
    if resultado % 2 == 0:
        print(resultado, 'Resultado é par...')
    else:
        print(resultado, 'Resultado é impar...')
    if resultado >= 0:
        print(resultado, 'Resultado é positivo')
    else:
        print(resultado, 'Resultado é negativo')
    if round(resultado) == resultado:
        print(resultado, 'É um numero inteiro')
    else:
        print(resultado, 'É um numero decima')

if operação == '-':
    resultado = float(num1) - float(num2)
    if resultado % 2 == 0:
        print(resultado, 'Resultado é par...')
    else:
        print(resultado, 'Resultado é impar...')
    if resultado >= 0:
        print(resultado, 'Resultado é positivo')
    else:
        print(resultado, 'Resultado é negativo')
    if round(resultado) == resultado:
        print(resultado, 'É um numero inteiro')
    else:
        print(resultado, 'É um numero decima')

if operação == '*':
    resultado = float(num1) * float(num2)
    if resultado % 2 == 0:
        print(resultado, 'Resultado é par...')
    else:
        print(resultado, 'Resultado é impar...')
    if resultado >= 0:
        print(resultado, 'Resultado é positivo')
    else:
        print(resultado, 'Resultado é negativo')
    if round(resultado) == resultado:
        print(resultado, 'É um numero inteiro')
    else:
        print(resultado, 'É um numero decima')

if operação == '/':
    resultado = float(num1) / float(num2)
    if resultado % 2 == 0:
        print(resultado, 'Resultado é par...')
    else:
        print(resultado, 'Resultado é impar...')
    if resultado >= 0:
        print(resultado, 'Resultado é positivo')
    else:
        print(resultado, 'Resultado é negativo')
    if round(resultado) == resultado:
        print(resultado, 'É um numero inteiro')
    else:
        print(resultado, 'É um numero decima')