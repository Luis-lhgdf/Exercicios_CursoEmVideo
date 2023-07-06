# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
cont = soma = 0
while True:
    nun = int(input("DIGITE UM VALOR: "))
    if nun == 999:
        break
    cont +=1
    soma +=nun
print(f"VOCE INFORMOU {cont} VALORES E A SOMA ENTRE ELES É {soma}")

