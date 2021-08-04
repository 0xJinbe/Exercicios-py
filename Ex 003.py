"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

area = float(input('Coloque a área a ser pintada em metros quadrados: '))
rendimento = area/3
preço_litro = 80/18
custo = rendimento*preço_litro
quantidade = rendimento/18

print('Quantidade de tinta a ser comprada: ', quantidade, 'Preço gasto: ', custo)
