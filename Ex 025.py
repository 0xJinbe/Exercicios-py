"""Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10."""

nt_1 = int(input('Entre com valor trimestre 1: '))
nt_2 = int(input('Entre com o valor trimesre 2: '))
nt_3 = int(input('Entre om o valor trimestre 3: '))

tt = nt_1 + nt_2 + nt_3
mm = tt / 3
print(mm)
if mm >= 7:
    print('Apr.')
else:
    print('Rep.')