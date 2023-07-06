# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de
# aumento.

s = int(input("INFORME SEU SALARIO ATUAL: "))
n = (15*s)/100
print("PARABENS, VOCE GANHOU UM AUMENTO DE 15%, SEU NOVO SALARIO PASSA SER AGORA {}R$ !!!".format(n+s))

