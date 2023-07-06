# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

geral = []
media_idade = []
soma_idade = 0
mulheres = list()
idade_acima_da_media = list()
while True:
    pessoa = {"NOME": str(input("DIGITE SEU NOME: ")).strip().upper(),
              "IDADE": int(input("DIGITE SUA IDADE: ")),
              "SEXO": str(input("DIGITE SEU SEXO [M/F]: ")).strip().upper()[0]}
    while pessoa["SEXO"] not in "MF":
        pessoa["SEXO"] = str(input("OPÇÃO INVALIDA ... DIGITE SEU SEXO [M/F]: ")).strip().upper()[0]
    geral.append(pessoa)
    if pessoa["SEXO"] == "F":
        mulheres.append(pessoa)

    resp = str(input("QUER CONTINUAR O CADASTRO: [S/N]: ")).strip().upper()[0]

    while pessoa["SEXO"] not in "MF":
        pessoa["SEXO"] = str(input("OPÇÃO INVALIDA ... DIGITE SEU SEXO [M/F]: ")).strip().upper()[0]
    while resp not in "SN":
        resp = str(input("OPÇÃO INVALIDA ... QUER CONTINUAR O CADASTRO?: [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
print(geral)
