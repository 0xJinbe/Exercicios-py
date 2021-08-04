"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato."""

n_eleitores = int(input('Qual o numero total de eleitores? '))
l_candidatos = []

count_A = 0
count_B = 0
count_C = 0
n_repetições = 0
while n_repetições < n_eleitores:
    voto = (input('Qual candidato deseja votar? A,B,C: ')).upper()
    l_candidatos.append(voto)
    n_repetições += 1
print(l_candidatos)

for i in l_candidatos:
    if i == 'A':
        count_A += 1
    elif i == 'B':
        count_B += 1
    else:
        count_C += 1

print(f"A quantidade de pessoas que votou no candidato A é de: {count_A}. Candidato B: {count_B}. Candidato C: {count_C}")


