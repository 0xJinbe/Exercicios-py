"""Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos."""

turmas = int(input('Entre com a quantidade de turmas: '))
lista = []
count = 0

while count < turmas:
    alunos = int(input('Quantidade de alunos: '))
    count += 1
    if alunos < 40:
        lista.append(alunos)
    else:
        print('A quantidade de alunos por turma deve ser menor que 40...')

media = sum(lista)/len(lista)
print(f"A media dos alunos é de: {media}")




"""
turmas = int(input('Digite a quantidade de turmas: '))
alunos_turmas = []
turma = 1

for i in range(turmas):
    print(f"turma, {turma}")
    alunos = int(input('Alunos da turma: '))
    while alunos > 40:
        print('turma ', turma, " [ uma turma so pode ter 40 alunos ]")
        alunos = int(input('Alunos da turma: '))
    turma += 1
    alunos_turmas.append(alunos)
media = sum(alunos_turmas)/len(alunos_turmas)
print('A media é igual a: ', media)"""