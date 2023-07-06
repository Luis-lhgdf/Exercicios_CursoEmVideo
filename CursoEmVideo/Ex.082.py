# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []
while True:
    valores = int(input("DIGITE UM NUMERO: "))
    lista.append(valores)
    resp = str(input("QUER CONTINUAR? [S/N]: ")).strip().upper()[0]
    while resp not in "SN":
        resp = str(input("RESPOSTA INVALIDA ... QUER CONTINUAR? [S/N]: ")).strip().upper()[0]
    if resp == 'N':
        break
for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(lista)
print(pares)
print(impares)
