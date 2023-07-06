# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0

for c in range(1, 6, 1):
    pesos = float(input("INFORME O PESO DA {}PESSOA: ".format(c)))
    if c == 0:
        maior = pesos
        menor = pesos
    if pesos > maior:
        maior = pesos
    if pesos < menor:
        menor = pesos

print("O MAIOR PESO É {} E O MENOR PESO É {}".format(maior, menor))
