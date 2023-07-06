# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando
# o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

# Exercício Python 35. Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
# podem ou não formar um triângulo.

r1 = float(input("VALOR DA RETA 1: "))
r2 = float(input("VALOR DA RETA 2: "))
r3 = float(input("VALOR DA RETA 3: "))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print("\033[1;31;00m PODE FORMAR UM TRIANGULO \033[m", end="")
    if r1 == r2 == r3:
        print("EQUILATERO")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISÓSCELES")

else:
    print("NÃO PODE SER UM TRIANGULO :(")
