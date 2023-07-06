# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter
jogo = {"jogador 1": randint(1, 6), "jogador 2 ":randint(1, 6), "jogador 3 ": randint(1, 6), "jogador 4 ": randint(1, 6)}
ordenado = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("{:-^50}".format("RANKING DOS JOGADORES"))
for i, v in enumerate(ordenado):
    print(f"{i+1}° {v[0]}  com {v[1]} pontos".upper())
