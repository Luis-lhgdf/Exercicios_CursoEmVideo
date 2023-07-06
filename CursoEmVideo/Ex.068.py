# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

vitoria = 0
while True:
    pc = randint(0, 10)
    player = int(input("INFORME UM VALOR: "))
    soma = player + pc
    perg = " "
    while perg not in "PI":
        perg = str(input("PAR OU IMPAR [P/I]: ")).strip().upper()[0]
    print(f"VOCE: {player} --> PC: {pc} --> SOMA: {soma}")
    print("PAR" if soma % 2 == 0 else "IMPAR")
    if perg == "P":
        if soma % 2 == 0:
            vitoria +=1
            print("VOCE VENCEU")
            print("VAMOS JOGAR NOVAMENTE...")
        else:
            print("VOCE PERDEU")
            print(f"GAME OVER, VOCE VENCEU {vitoria}X")
            break
    if perg == "I":
        if soma % 2 != 0:
            vitoria += 1
            print("VOCE VENCEU")
            print("VAMOS JOGAR NOVAMENTE...")
        else:
            print("VOCE PERDEU")
            print(f"GAME OVER, VOCE VENCEU {vitoria}X")
            break
print("FIM")
