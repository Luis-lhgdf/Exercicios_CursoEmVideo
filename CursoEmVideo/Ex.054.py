# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime

ano_atual = datetime.date.today().year
ano_de_maior = ano_atual-18
maioridade = 0
menoridade = 0

for c in range(1, 8, 1):
    pessoas = int(input("DIGITE O ANO DE NASCIMENTO DA {}° PESSOA: ".format(c)))
    if pessoas <= ano_de_maior:
        maioridade +=1
    else:
        menoridade +=1
print("EXISTEM {} PESSOAS MAIOR DE IDADE E {} PESSOAS MENOR DE IDADE".format(maioridade, menoridade))

