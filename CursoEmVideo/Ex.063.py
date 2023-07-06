# Exercício Python 63: escreva um programa que leia um número N inteiro qualquer e mostre na tela
# os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

# 0 – 1 – 1 – 2 – 3 – 5 – 8
print("GERADOR DE SEQUENCIA FIBONACCI")
c = 0
t1 = 0
t2 = 1
n = int(input("QUANTOS TERMOS VOCE QUER VISUALIZAR: "))
print("{} -> {}".format(t1, t2), end="")
while c <=n:
    t3 = t1 + t2
    print(" -> {}".format(t3), end="")
    t1 = t2
    t2 = t3
    c +=1
print(" -> fim")
