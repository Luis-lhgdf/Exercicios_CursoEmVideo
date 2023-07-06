# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.


n1 = int(input("DIGITE O 1° VALOR: "))
n2 = int(input("DIGITE O 2° VALOR: "))
lista = [1, 2, 3, 4, 5]


print("""OQUE GOSTARIA DE FAZER COM ESSES DOIS VALORES:\n 
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa""")
resp = int(input("DIGITE A OPÇÃO DESEJADA: "))

while resp not in lista:
    resp = int(input("DIGITE UMA OPÇÃO VALIDA: "))
if resp == 1:
    print("A SOMA ENTRE {} E {} = {}".format(n1, n2, n1+n2))

if resp == 2:
    print("A MULTIPLICAÇÃO ENTRE {} E {} = {}".format(n1, n2, n1 * n2))

if resp == 3:
    print("O MAIOR ENTRE {} E {} = {}".format(n1, n2, max(n1, n2)))

if resp == 4:
    while resp == 4:
        n1 = int(input("DIGITE O 1° VALOR: "))
        n2 = int(input("DIGITE O 2° VALOR: "))
        lista = [1, 2, 3, 4, 5]

        print("""OQUE GOSTARIA DE FAZER COM ESSES DOIS VALORES:\n 
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa""")
        resp = int(input("DIGITE A OPÇÃO DESEJADA: "))

        while resp not in lista:
            resp = int(input("DIGITE UMA OPÇÃO VALIDA: "))
        if resp == 1:
            print("A SOMA ENTRE {} E {} = {}".format(n1, n2, n1 + n2))
        if resp == 2:
            print("A MULTIPLICAÇÃO ENTRE {} E {} = {}".format(n1, n2, n1 * n2))
        if resp == 3:
            print("O MAIOR ENTRE {} E {} = {}".format(n1, n2, max(n1, n2)))
if resp == 5:
    print("PROGRAMA ENCERRADO, MUITO OBRIGADO")

