# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista = []
temp = []
n = []
while True:
    temp.append(str(input("NOME: ")).strip().upper())
    temp.append(float(input("NOTA 1: ")))
    temp.append(float(input("NOTA 2: ")))
    lista.append(temp[:])
    temp.clear()
    resp = str(input("QUER CONTINUAR? [S/N]: ")).strip().upper()[0]
    while resp not in "SN":
        resp = str(input("QUER CONTINUAR? [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
print(f"N°    NOMES                MÉDIA")
for i, aluno in enumerate(lista):
    print(f"{i:.<5} {aluno[0]:.<20} {(aluno[1]+aluno[2])/2}", end="")
    print()
while True:
    print("DIGITE 999 PARA FINALIZAR O PROGRAMA")
    nun = int(input("INFORME O N° DO ALUNO PARA RETORNAR SUAS NOTAS: "))
    if nun == 999:
        break
    while nun > len(lista)-1:
        print("DIGITE 999 PARA FINALIZAR O PROGRAMA")
        nun = int(input("NUMERO INVALIDO ... INFORME O N° DO ALUNO PARA RETORNAR SUAS NOTAS: "))
    if nun <= len(lista)-1:
        print(f"ALUNO: {lista[nun][0]}\nNOTA 1 = {lista[nun][1]}\nNOTA 2 = {lista[nun][2]}")
