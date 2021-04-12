"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente."""


qt_mo = float(input('Quantos kgs de morango? '))
qt_ma = float(input('Quantos kgs de maça? '))
p_mo = 0
p_ma = 0
if qt_mo < 5:
    p_mo = qt_mo * 2.50
else:
    p_mo = qt_mo * 2.20

if qt_ma < 5:
    p_ma = qt_ma * 1.80
else:
    p_ma = qt_ma *  1.50
p_geral = p_mo + p_ma


if qt_mo + qt_ma >= 8 or p_geral > 25:
    p_geral = p_geral - (p_geral*0.10)

print('Valor a ser pago: ', p_geral)