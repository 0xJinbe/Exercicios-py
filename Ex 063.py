"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas."""


n_temp = int(input('Qual a quantidade de temperaturas? '))
temp = []

for i in range (n_temp):
    temperatura = temp.append(float(input('Entre com a temperatura: ')))
    
print(f"Maior: {max(temp)} Menor: {min(temp)} Media: {sum(temp)/len(temp)}")