# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

nun = int(input("INFORME UM NUMERO DE 0 A 9999: "))
print("milhar {}\ncentena {}\ndezena {}\nunidade {}\n ".format(nun//1000 % 10, nun//100 % 10, nun//10 % 10, nun//1 % 10))






