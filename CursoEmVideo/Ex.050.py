# Exercício Python 50: desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
for c in range(1, 7, 1):
    nun = int(input("DIGITE O {}° NUMERO INTEIRO: ".format(c)))
    if nun % 2 == 0:
        soma +=nun

print(soma)
