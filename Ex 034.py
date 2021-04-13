"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido."""

nt = int(input('Entre com uma nota (0 a 10):  '))

while (nt > 0) and (nt < 10):
    nt = int(input('Entre com uma nota (0 a 10):  '))
