# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input("INFORME SEU SEXO - [M/F]: ").strip().upper()[0])

while sexo not in "MmFf":
    sexo = str(input("DADOS INVALIDOS, POR FAVOR INFORME SEU SEXO - [M/F]: ").strip().upper()[0])

print("SEXO {} REGISTRADO COM SUCESSO".format(sexo))


