"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

l_vendidos = float(input('Quantos litros foram vendidos? : '))
comb = input('Qual é o tipo de combustível? (alcooll = a, gasolina = g): ').lower()
p_litros = 0

if comb == 'a':
    p_litros = 1.90
    if l_vendidos <= 20:
        l_vendidos = l_vendidos - (l_vendidos*0.03)
    else:
        l_vendidos = l_vendidos - (l_vendidos*0.05)
else:
    p_litros = 2.50
    if l_vendidos <= 20:
        l_vendidos = l_vendidos - (l_vendidos*0.04)
    else:
        l_vendidos = l_vendidos - (l_vendidos*0.06)
preço = l_vendidos*p_litros
print('Preço a pagar é: ', preço,"R$")