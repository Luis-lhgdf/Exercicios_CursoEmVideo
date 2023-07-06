# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {"NOME": str(input("DIGITE O NOME DO JOGADOR: ")).strip().upper()}
resp = int(input("QUANTAS PARTIDAS ELE JOGOU: "))
gol = []
total = 0
for c in range(0, resp):
    a = int(input(f"QUANTOS GOLS ELE FEZ NA {c+1}° PARTIDA: "))
    gol.append(a)

    total += a
jogador["GOLS"] = gol
jogador["SALDO DE GOLS"] = total
print("=-" * 50)
print(jogador)
print("=-" * 50)
for k, v in jogador.items():
    print(f"O CAMPO {k} TEM O VALOR: {v}")
print("=-" * 50)
print(f"O JOGADOR {jogador['NOME']} JOGOU {resp} PARTIDAS")
for i, v in enumerate(gol):
    print(f"NA PARTIDA {i+1}, FEZ {v} GOLS")
print(f"FOI UM TOTAL DE {total}")
