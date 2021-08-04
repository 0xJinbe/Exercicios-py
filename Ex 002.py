"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido."""

ganho_hr = float(input('Quanto se ganha por hora? '))
qt_hrs = float(input('Quantas horas sao trabalhadas por mẽs? '))

bruto = ganho_hr*qt_hrs
print(bruto)
ir = (bruto*0.11)
inss = (bruto*0.08)
sindicato = (bruto*0.05)
liquido = bruto-ir-inss-sindicato
print('Seu sal bruto é: ', bruto, 'Descontos: IR-INSS-sindicato:', ir,inss,sindicato, 'Sal liquido é: ', liquido )