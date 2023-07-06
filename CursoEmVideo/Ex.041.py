# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, conforme a idade:

# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

import datetime
data_atual = datetime.date.today()
ano_atual = data_atual.year

ano = int(input("DIGITE SEU ANO DE NASCIMENTO: "))
idade = ano_atual - ano

mirim = range(1, 9)
infantil = range(10, 14)
junior = range(15, 19)
senior = range(20, 25)

if idade in mirim:
    print("O ATLETA TEM {} ANOS E SE ENCAIXA NA CATEGORIA MIRIM".format(idade))
elif idade in infantil:
    print("O ATLETA TEM {} ANOS E SE ENCAIXA NA CATEGORIA INFANTIL".format(idade))
elif idade in junior:
    print("O ATLETA TEM {} ANOS E SE ENCAIXA NA CATEGORIA JÚNIOR".format(idade))
elif idade in senior:
    print("O ATLETA TEM {} ANOS E SE ENCAIXA NA CATEGORIA SENIOR".format(idade))
else:
    print("O ATLETA TEM {} ANOS E SE ENCAIXA NA CATEGORIA MASTER".format(idade))


