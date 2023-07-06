# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
soma = 0
acima_mil = 0
nome_p_barato = " "
cont = 0
valor_barato = 0
while True:
    resp = " "
    nome = str(input("NOME DO PRODUTO: ")).strip().upper()
    valor = float(input("VALOR DO PRODUTO: "))
    cont +=1
    soma += valor
    if cont == 1:
        valor_barato = valor
        nome_p_barato = nome
    if valor < valor_barato:
        valor_barato = valor
        nome_p_barato = nome
    if valor > 1000:
        acima_mil+=1
    while resp not in "SN":
        resp = str(input("QUER CONTINUAR: [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
print(f"VOCE GASTOU UM TOTAL DE R${soma} REAIS")
print(f"SENDO {acima_mil} PRODUTOS ACIMA DE R$1000 REAIS")
print(f"E O PRODUTO MAIS BARATO É O {nome_p_barato} CUSTANDO R${valor_barato} REAIS")

