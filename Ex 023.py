"""Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida."""

valida = False

dia = int(input('Entre com uma dia: '))
mes = int(input('Entre com uma mes: '))
ano = int(input('Entre com uma dia: '))

#mes com 31 dias
if ( mes == 1 or mes == 3 or mes ==5 or mes == 7 or mes == 8 or mes == 10 or mes ==12):
    if(dia<=31):
        valida = True
#meses com 30 dias
elif ( mes==4 or mes==6 or mes==9 or mes==11):
    if(dia<=30):
        valida = True
elif mes==2:
    #testa se e bissexto
    if (ano%4==0 and ano%100!=0) or (ano%400==0):
        if(dia<=29):
            valida = True
    elif(dia<=28):
        valida = True
if (valida):
    print('Data válida...')
else:
    print('Inválida...')