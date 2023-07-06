# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(jogador="desconhecido", gol=0):
    print(jogador, gol)


player = str(input("NOME DO JOGADOR: ").strip().capitalize())
gols = str(input("GOLS MARCADOS: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if len(player) ==0:
    player = "desconhecido"

ficha(player, gols)

