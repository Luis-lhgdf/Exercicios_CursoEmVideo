# Exercício Python 2: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = str(input("DIGITE SEU NOME: ")).strip().capitalize()
while len(nome) <=0:
    nome = str(input("DIGITE SEU NOME: ")).strip().capitalize()
else:
    print(f'Bem vindo {nome}, um enorme prazer ter voce conosco!')