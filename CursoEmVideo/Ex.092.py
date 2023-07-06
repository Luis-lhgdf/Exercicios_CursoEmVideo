# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
import datetime

anoatual = datetime.date.today().year
pessoa = {"NOME": str(input("DIGITE SEU NOME: ")).strip().upper(),
          "ANO DE NASCIMENTO": int(input("DIGITE O ANO DE NASCIMENTO: ")),
          "CARTEIRA DE TRABALHO": int(input("DIGITE A CTPS: "))
          }
pessoa["IDADE"] = anoatual - pessoa["ANO DE NASCIMENTO"]
if pessoa["CARTEIRA DE TRABALHO"] == 0:
    for k, v in pessoa.items():
        print(f"{k} TEM O VALOR {v}")
else:
    pessoa["ANO DE CONTRATAÇÃO"] = int(input("DIGITE O ANO DE CONTRATAÇÃO: "))
    pessoa["SALARIO"] = int(input("DIGITE SEU SALARIO: "))
    pessoa["IDADE APOSENTADORIA"] = (pessoa["ANO DE CONTRATAÇÃO"] + 35) - pessoa["ANO DE NASCIMENTO"]
    for k, v in pessoa.items():
        print(f"{k} TEM O VALOR {v}")
