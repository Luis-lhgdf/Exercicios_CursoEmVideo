# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = list()
while True:
    valores = int(input("DIGITE UM VALOR INT: "))
    if valores in lista:
        print("Valor duplicado!!! não irei adicionar")
        resp = str(input("QUER CONTINUAR? [S/N]")).upper().strip()[0]
        if resp not in "SN":
            print("RESPOSTA INVALIDA DIGITE NOVAMENTE")
            resp = str(input("QUER CONTINUAR? [S/N]")).upper().strip()[0]
        if resp == "N":
            break

    if valores not in lista:
        lista.append(valores)
        print('Valor adicionado com sucesso: ')
        resp = str(input("QUER CONTINUAR? [S/N]")).upper().strip()[0]
        if resp not in "SN":
            print("RESPOSTA INVALIDA DIGITE NOVAMENTE")
            resp = str(input("QUER CONTINUAR? [S/N]")).upper().strip()[0]
        if resp == "N":
            break
lista.sort()
print(lista)



