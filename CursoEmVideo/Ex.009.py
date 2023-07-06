# Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

valor = int(input("DIGITE UM VALOR:"))

for c in range(0, valor):
    print(f"{c} x {valor} = {c * valor}")
