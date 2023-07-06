# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
cont = 0

while True:
    valor = int(input("DIGITE UM VALOR: "))
    cont +=1
    lista.append(valor)
    resp = str(input("QUER CONTINUAR [S/N]: ")).upper().strip()[0]
    while resp not in "SN":
        resp = str(input("QUER CONTINUAR [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
print(lista)
print(len(lista))
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print(f"O VALOR 5 FAZ PARTE DA LISTA")
else:
    print("O VALOR 5 NÃO FAZ PARTE DA LISTA")


