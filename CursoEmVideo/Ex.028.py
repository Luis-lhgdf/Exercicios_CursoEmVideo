# Exercício Python 28: escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.


import random
from time import sleep
print(20*">=")
print("           JOGO DE ADVINHAÇÃO")
print(20*">=")

print("TENTE ADIVINHAR O NUMERO EM QUE ESTOU PENSANDO ENTRE 0 A 5")
print("PROCESSANDO...")
sleep(3)
print("")
print('JA ESCOLHI, TENTE ADIVINHAR!!!')
print("")

nun = int(input("QUAL NUMERO EU PENSEI? "))
pc = random.randint(0, 5)
if pc == nun:
    print("UAU, VOCÊ ACERTOU PARABÉNS!!!")
else:
    print("HAHAHA, VOCÊ ERROU EU PENSEI NO NUMERO {} E NÃO NO {}".format(pc, nun))
print("")
print(20*">=")
print("                GAME OVER")
print("PRESSIONE 'ALT + F11' PARA JOGAR NOVAMENTE")
print(20*">=")
