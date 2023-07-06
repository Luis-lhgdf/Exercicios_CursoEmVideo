# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo sem considerar espaços
# – Quantas letras tem o primeiro nome.

nome = str(input("DIGITE O SEU NOME: "))
print(nome.upper())
print(nome.lower())
es = (nome.count(" "))
tam = len(nome)
print(tam - es)
print(nome.find(" "))






