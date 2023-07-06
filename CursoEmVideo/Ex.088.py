# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
# para cada jogo, cadastrando tudo em uma lista composta.
import random
import time
lista = []
temp = [0, 0, 0, 0, 0, 0]
resp = int(input("quantos jogos serão gerados? "))
for c in range(0, resp):
    for sorteio in range(0, 6):
        valor = random.randint(1, 60)
        if valor not in temp:
            temp[sorteio] = valor
    temp.sort()
    lista.append(temp[:])
for c in range(0, resp):
    print(f"JOGO[{c+1}] = {lista[c]}", end="")
    time.sleep(1)
    print()
print("{:-^35}".format("BOA SORTE"))