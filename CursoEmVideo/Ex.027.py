# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
# último nome separadamente.

nome = str(input("Digite o seu Nome completo: ")).capitalize()
e = nome.find(" ")
p = nome[:e]
ue = nome.rfind(" ")
u = nome[ue:]
print(" SEU 1° NOME É {} E SEU ULTIMO NOME É {}".format(p.strip(), u.strip()))


