# Exercício Python 101: Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
import datetime


def voto(ano):
    ano_atual = datetime.date.today().year
    idade = ano_atual - ano
    if idade <= 18:
        print(F"COM {idade} ANOS O VOTO É OPCIONAL")
    elif 19 <= idade <= 69:
        print(F"COM {idade} ANOS O VOTO É OBRIGADO")
    else:
        print(F"COM {idade} ANOS O VOTO É OPCIONAL")

