"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""


nome = input('Entre com o nome: ')
senha = input('Entre com uma senha: ')

while nome == senha:
    print('ERRO: o usuario nao pode ser igual a senha.')
    nome = input('Entre com o nome: ')
    senha = input('Entre com uma senha: ')
else:
    print('Cadastro feito com sucesso')

