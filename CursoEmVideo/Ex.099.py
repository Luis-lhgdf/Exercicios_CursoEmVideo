# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. Seu programa tem que analisar
# todos os valores e dizer qual deles é o maior

def maior(* valor):
    lista = []
    for v in valor:
        lista.append(v)
    m = max(lista)
    print(f"O maior valor digitado foi {m}")

