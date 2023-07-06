# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

tot = 0
nun = int(input("DIGITE UM VALOR INTEIRO: "))
for c in range (1, nun + 1):
    if nun % c ==0:
        print("\033[1;33m", end="")
        tot += 1
    else:
        print("\033[1;31m", end="")
    print("{}".format(c), end="")
print("\033[m o numero {} foi divisivel {}x".format(nun, tot))
if tot == 2:
    print("e por isso ele é primo")
else:
    print("e por isso ele nao é primo")
