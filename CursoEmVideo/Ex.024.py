# Exercício Python 24: crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

city = str(input("INFORME O NOME DE SUA CIDADE: ")).upper()
e = city.find(" ")
c = city[:e]
print(c == "SANTO")
