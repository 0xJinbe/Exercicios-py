"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

tp = input('Qual o tipo de carne deseja comprar: (a)->File duplo; (b)--> Alcatra, (c)-->Picanha')
qt = float(input('Qual a quantidade de carne a ser comprada: '))
tbj = input('Compra feita com cartao Tabajara? (s/n): ').lower()

p_total = 0
v_desconto = 0
v_a_pagar = 0

if tp == 'a':
    if qt < 5:
        p_total = (qt * 4.90)
    else:
        p_total = (qt * 5.80)
if tp == 'b':
    if qt < 5:
        p_total = (qt * 5.90)
    else:
        p_total = (qt * 6.80)
if tp == 'c':
    if qt < 5:
        p_total = (qt * 6.90)
    else:
        p_total = (qt * 7.80)

if tbj == 's':
    v_desconto = (p_total * 0.05)
else:
    p_total = p_total

v_a_pagar = p_total - v_desconto

#tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
print('Cupom fiscal...','\n', 'TIPO: ', tp.title(),'\n', 'QUANTIDADE: ', qt,'\n', 'PREÇO TOTAL: ', p_total,'\n', 'TIPO DE PAGAMENTO: ', 'Cartão tabajara?', tbj,'\n', 'VALOR DO DESCONTO: ', v_desconto,'\n', 'VALOR A PAGAR: ', v_a_pagar)