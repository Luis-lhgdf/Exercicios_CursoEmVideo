# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = []
gol = []
total = 0
jogador = {}
while True:
    jogador = {"NOME": str(input("DIGITE O NOME DO JOGADOR: ")).strip().upper()}
    resp = int(input("QUANTAS PARTIDAS {} JOGOU?:  ".format(jogador["NOME"])))
    if resp == 0:
        break
    else:
        for c in range(0, resp):
            gol.append(int(input(f"    QUANTOS GOLS FEZ NA {c+1}° PARTIDA: ")))
        for g in gol:
            total +=g
    jogador["GOLS"] = gol
    jogador["SALDO DE GOLS"] = total
    time.append(jogador.copy())
    gol = []

    jogador.clear()

    total = 0

    resp2 = str(input("QUER CONTINUAR O CADASTRO? [S/N]: ")).strip().upper()[0]
    while resp2 not in "SN":
        resp2 = str(input("OPÇÃO INVALIDA ... QUER CONTINUAR O CADASTRO? [S/N]: ")).strip().upper()[0]
    if resp2 == "N":
        break

print(50 * "=-")
print("COD   NOME       GOLS          TOTAL")
print(50 * "-")
for i, v in enumerate(time):
    print(f"{i:.<5} {v['NOME']:.<10} {v['GOLS']}{5* '-'} {v['SALDO DE GOLS']}")
print(50 * "-")
while True:
    resp3 = int(input("MOSTRAR DADOS DE QUAL JOGADOR? (999 PARA PARAR): "))
    if resp3 == 999:
        break
    else:
        print(f"LEVANTAMENTO DO JOGADOR {time[resp3]['NOME']}")
        for i, p in enumerate(time[resp3]['GOLS']):
            print(f" NO JOGO {i+1} FEZ {p}.")
print(F"{'FIM DO PROGRAMA, VOLTE SEMPRE':-^50}")
