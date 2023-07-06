# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

cadastro = []
maiorP = []
menorP = []


def leiafloat(msg):
    while True:
        try:
            nun = float(input(msg))
        except Exception as erro:
            print(f"HOUVE UM ERRO DE --> \033[31m{erro}\033[m <---, TENTE NOVAMENTE:")
            continue
        else:
            return nun


def leiaNome(msg):
    try:
        nome = str(input(msg).strip().capitalize())
        while len(nome) <= 0 or not nome.isalpha():
            print("Valor invalido, digite novamente: ")
            nome = str(input(msg).strip().capitalize())
    except Exception as erro:
        print(f"Houve um erro ao adicionar o nome: {erro} ")
    else:
        return nome


while True:
    pessoas = {'nome': leiaNome("DIGITE SEU NOME: ").strip().capitalize(), 'peso': leiafloat("DIGITE SEU PESO: ")}
    cadastro.append(pessoas.copy())
    pessoas.clear()
    while True:
        resp = str(input("DESEJA CONTINUAR? S/N: ").strip().upper())
        while resp not in "SN":
            resp = str(input("DESEJA CONTINUAR? S/N: ").strip().upper())
        if resp == "S":
            break
        if resp == "N":
            break
    if resp == "N":
        break
total_p = len(cadastro)

for i, cadastros in enumerate(cadastro):
    if cadastros['peso'] >= 80:
        maiorP.append(cadastros['nome'])
    if cadastros['peso'] <= 50:
        menorP.append(cadastros['nome'])

print(cadastro)
print(f"Existe um total de {total_p} Pessoas Cadastradas")
print(f"Lista de nomes das pessoas mais leves:{menorP} ")
print(f"Lista de nomes das pessoas mais pesadas:{maiorP} ")