# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math

while True:
    try:
        nun = int(input("DIGITE UM VALOR: "))
    except ValueError:
        print("ocorreu um erro")
        continue
    else:
        print(
            f"VOCE ESCOLHEU O VALOR: {nun}\nO DOBRO É {nun * 2}, SEU TRIPLO É {nun * 3} E SUA RAIZ QUADRADA É {math.isqrt(nun)} ")
        break
