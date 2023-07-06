# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = 0
soma = 0
nun = int(input("DIGITE UM VALOR: "))
while nun != 999:
    cont +=1
    soma += nun
    nun = int(input("DIGITE UM VALOR: "))
print("TEVE UM TOTAL DE {} VALORES DIGITADOS E A SOMA É {}!".format(cont, soma))

