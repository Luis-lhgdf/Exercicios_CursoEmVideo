# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

f = 1
c = int(input("DIGITE UM VALOR: "))
while c > 0:
    print(c, end="")
    print(" X "if c > 1 else " = ", end="")
    f *= c
    c -= 1

print(f)

