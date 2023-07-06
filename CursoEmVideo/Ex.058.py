# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Porém, agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
from time import sleep
palpites = 0

print(20*">=")
print("           JOGO DE ADVINHAÇÃO")
print(20*">=")

print("TENTE ADIVINHAR O NUMERO EM QUE ESTOU PENSANDO ENTRE 0 A 10")
print("PROCESSANDO...")
sleep(1.5)
print("")
print('JA ESCOLHI, TENTE ADIVINHAR!!!')
print("")

nun = int(input("QUAL NUMERO EU PENSEI? "))
pc = random.randint(0, 10)
while nun != pc:
    if nun < pc:
        dica = "MAIS"
    elif nun > pc:
        dica = "MENOS"
    print("HAHAHA, VOCÊ ERROU ESTA PARA {}".format(dica))
    nun = int(input("QUAL SEU PROXIMO PALPITE? "))
    palpites += 1
print("MUITO BEM VOCE ACERTOU, EU REALMENTE PENSEI NO {}".format(pc))
print("VOCE PRECISOU DE {} TENTATIVAS PARA ACERTAR".format(palpites+1))
print("")
print(20*">=")
print("                GAME OVER")
print("PRESSIONE 'ALT + F11' PARA JOGAR NOVAMENTE")
print(20*">=")



