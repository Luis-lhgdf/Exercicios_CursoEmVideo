# Exercício Python 51: desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input("DIGITE O PRIMEIRO TERMO: "))
razao = int(input("DIGITE A RAZÃO: "))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo+razao, razao):
    print(c)


















