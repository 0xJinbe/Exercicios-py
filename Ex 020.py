"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;"""

l1 = float(input('Lado um do triangulo: '))
l2 = float(input('Lado dois do triangulo: '))
l3 = float(input('Lado tres do triangulo: '))

if l1 + l2 >= l3:
    print('É um triangulo')
    if l1 == l2 == l3:
        print('Equilátero')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Isósceles')
    else:
        print('Escaleno')

else:
    print('Não é um triangulo')

