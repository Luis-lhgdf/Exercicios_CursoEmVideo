# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('DIGITE O VALOR DO CATETO OPOSTO: '))
ca = float(input("DIGITE O VALOR DO CATETO ADJASCENTE: "))
h = hypot(co, ca)
print("o valor da hipotenusa é {:.2f}". format(h))



