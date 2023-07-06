# Exercício Python 56: desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media_do_grupo = 0
nome_do_homem_mais_velho = ""
idade_do_homem_mais_velho = 0
qtd_mulheres_menos_de_20_anos = 0
for c in range(1, 5, 1):
    print("           DADOS DA {}° PESSOA:".format(c))
    print(20 * "=-")
    nome = str(input("DIGITE O NOME: ")).strip().upper()
    idade = int(input("DIGITE A IDADE: "))
    sexo = str(input("DIGITE O SEXO: [(M) OU (F)]: ")).strip().upper()
    media_do_grupo += idade
    if c == 1 and idade > idade_do_homem_mais_velho and sexo == "M":
        idade_do_homem_mais_velho = idade
        nome_do_homem_mais_velho = nome
    if sexo == "M" and idade > idade_do_homem_mais_velho:
        idade_do_homem_mais_velho = idade
        nome_do_homem_mais_velho = nome
    if c == 1 and idade < 20 and sexo == "F":
        qtd_mulheres_menos_de_20_anos += 1
    if sexo == "F" and idade < 20:
        qtd_mulheres_menos_de_20_anos += 1

print("A MÉDIA DE IDADE DO GRUPO É {}".format(media_do_grupo / 2))
print("O HOMEM MAIS VELHO DO GRUPO SE CHAMA {} E ELE TEM {} ANOS".format(nome_do_homem_mais_velho, idade_do_homem_mais_velho))
print("EXISTEM {} MULHERES MENOS DE 20 ANOS DE IDADE".format(qtd_mulheres_menos_de_20_anos))
