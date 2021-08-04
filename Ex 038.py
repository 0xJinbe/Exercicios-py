"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação"""

cidade_a = int(input('Entre com a população da primeira cidade: '))
cidade_b = int(input('Entre com a população da segunda cidade: '))
ano = 0
tx_a = float(input('Entre com a primeira taxa de crescimento (em %): '))
tx_b = float(input('Entre com a segunda taxa de crescimento(em %): '))

while cidade_a <= cidade_b:
    cidade_a += (cidade_a*tx_a)/100
    cidade_b += (cidade_b*tx_b)/100
    ano += 1
    print(f"A pop da cidade a {cidade_a}, a pop cidade b {cidade_b} o ano {ano}")
