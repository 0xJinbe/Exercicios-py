"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16"""

num = (input('Numero: '))
num_str = str(num)
qt_num = len(num_str)

if qt_num == 3:
    centena = num_str[0:1]
    dezena = num_str[1:2]
    unidade = num_str[2:3]
    print(num_str, '=', 'centena', centena, 'dezena', dezena, 'unidades', unidade)
if qt_num == 2:
    dezena = num_str[0:1]
    unidade = num_str[1:2]
    print(num_str, '=', 'dezena', dezena, 'unidades', unidade)
if qt_num == 1:
    unidade = num_str[0:1]
    print(num_str, '=', 'unidade', unidade)