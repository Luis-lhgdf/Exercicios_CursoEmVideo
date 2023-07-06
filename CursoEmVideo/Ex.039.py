# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# conforme a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

data_atual = datetime.date.today()
ano_atual = data_atual.year

ano = int(input("INFORME O ANO EM QUE VOCE NASCEU: "))
idade = ano_atual-ano
alist = 18
dif = idade - 18

if dif == 0:
    print("É A HORA EXATA DE VOCE SE ALISTAR, PROCURE A UNIDADE MAIS PROXIMA E REALIZE SEU CADASTRO!!!")
elif dif >0:
    print("O PRAZO JA ESTOUROU!!!, FAZ {} ANOS QUE VOCE DEVERIA TER SE ALISTADO, PROCURE A UNIDADE MAIS PROXIMA E REALIZE SEU CADASTRO".format(dif))
else:
    print("FIQUE TRANQUILO, AINDA FALTA {} ANOS PARA A DATA DE ALISTAMENTO MILITAR".format(dif*-1))

