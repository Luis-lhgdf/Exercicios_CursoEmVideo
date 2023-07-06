# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção
# Inteira.

from math import trunc

nun = float(input("INFORME UM VALOR PARA SABER SUA PORÇÃO INTEIRA: "))
print(int(nun))
print(trunc(nun))



