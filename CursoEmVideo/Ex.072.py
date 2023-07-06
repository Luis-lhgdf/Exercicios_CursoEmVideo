# Exercício Python 72: Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
extenso = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE", "DEZ")

while True:
    nun = int(input("DIGITE UM VALOR ENTRE 0 E 10: "))
    if 0 <= nun <= 10:
        print("VOCE DIGITOU {}".format(extenso[nun]))
        break

