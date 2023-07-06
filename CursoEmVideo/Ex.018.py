# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
a = float(input("DIGITE O VALOR DE UM ÂNGULO: "))
print("O SENO É {:.2f} O COSSENO é {:.2f} E A TANGENTE É {:.2f}".format(sin(radians(a)), cos(radians(a)), tan(radians(a))))

