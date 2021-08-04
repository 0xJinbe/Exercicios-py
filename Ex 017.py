"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220."""


hr = float(input('Qual o valor das horas trabalhadas? '))
qtn = float(input('Qual a quantidade de horas trabalhadas? '))

bruto = hr * qtn
print('Bruto: ', bruto)

fgts = (bruto*11)/100
print('FGTS: ', fgts)

inss = (bruto*10)/100
print('INSS: ', inss)

sindicato = (bruto*3)/100
print('Sindicato: ', sindicato)

ir = 0
if bruto <= 900:
    ir = 0
elif bruto <= 1500:
    ir = (5*bruto)/100
elif bruto <= 2500:
    ir = (10*bruto)/100
else:
    ir = (20*bruto)/100


descontos = ir + inss
liquido = bruto - descontos

print('Salario  bruto: ', bruto,'IR: ', ir, 'INSS: ', inss,'FGTS: ', fgts,'Descontos: ', descontos,'Total liquido: ', liquido)