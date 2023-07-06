# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("{:-^40}".format("BANCO CENTRAL LHGDF"))
valor = int(input("QUANTOS REAIS VOCE QUER SACAR? "))
cel = 50
contcel = 0
sobra = valor
while True:
    if sobra >=cel:  # nesse primeiro IF estamos analisando quantas notas de 50 reais conseguimos retirar do valor do input
        sobra -= cel
        contcel +=1
    else:  # este else esta sendo usado caso nao der mais para retirar o valor de 50 reais.
        if contcel > 0:
            print(f"TOTAL DE {contcel} CEDULAS DE R${cel}REAIS")
        if cel == 50:  # trocando para a nova cedula de 20
            cel = 20
        elif cel == 20:  # usando o ELIF, pq ele só vai acontecer se o IF de cima dor falso, então como a cedula de 20 nao foi possível retirar do valor do input, estamos atribuindo um novo valor, no caso a nota de 10 reais
            cel = 10
        elif cel == 10:
            cel = 1
        contcel = 0  # essa condição acontece toda vez que uma cedula nova é chamada, assim ela nao soma com a contagem da anterior
        if sobra == 0:  # agr como o valor final chegou a zero, precisamos finalizar o looping com o break
            break
print("fim")
