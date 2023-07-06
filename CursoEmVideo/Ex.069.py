# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.


print("{:-^70}".format("SISTEMA DE CADASTROS DE PESSOA FISICA"))
homens = 0
maior_18 = 0
mulheres_m_20 = 0
while True:
    sexo = " "
    resp = " "
    idade = int(input("INFORME A IDADE: "))
    while sexo not in "FM":
        sexo = str(input("INFORME O SEXO: [M/F]: ")).strip().upper()[0]

    if idade > 18:
        maior_18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres_m_20 += 1
    print("{:-^50}".format("CADASTRO REALIZADO COMO SUCESSO"))
    print(50 * "_")

    while resp not in "SN":
        resp = str(input("QUER CONTINUAR? [S/N]: ")).strip().upper()[0]

    if resp == "N":
        break
print("")
print("{:-^50}".format("RELATORIO DE CADASTRO"))
print("EXISTEM {} PESSOAS MAIORES DE 18 ANOS\nCOM O TOTAL DE {} HOMENS CADASTRADOS\nE {} MULHERES MENORES DE 20 ANOS DE IDADE".format(maior_18, homens, mulheres_m_20))
print("FIM")
