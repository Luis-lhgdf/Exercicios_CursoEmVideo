# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input("DIGITE O 1 NUMERO: "))
b = int(input("DIGITE O 2 NUMERO: "))
c = int(input("DIGITE O 3 NUMERO: "))

if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O MENOR VALOR É {}.".format(menor))
print("O MAIOR VALOR É {}.".format(maior))


