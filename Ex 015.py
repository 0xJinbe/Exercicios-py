"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""


inp = input('Entre com o periodo do dia : M-matutino ou V-Vespertino ou N- Noturno.  ').capitalize()

if inp == 'M':
    print('Bom dia!')
elif inp == 'V':
    print('Boa tarde!')
elif inp == 'N':
    print('Boa noite!')
else:
    print('Valor inválido.')