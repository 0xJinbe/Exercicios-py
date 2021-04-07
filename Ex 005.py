"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

arquivo = float(input('Qual o tamanho do arquivo para dowload(mb): '))
internet = float(input('Qual a velocidade da internet? '))

print('Tempo aproximado de donwload(min): ', ((arquivo/internet)*60 ))
