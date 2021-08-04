"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = input('Entre com a letra desejada: ').capitalize()

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print('A letra escohida é vogal.')
else:
    print('A letra escolhida é consoante.')

