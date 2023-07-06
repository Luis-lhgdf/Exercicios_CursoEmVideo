# Exercício Python 19: um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
a1 = str(input("NOME DO ALUNO 1: "))
a2 = str(input("NOME DO ALUNO 2: "))
a3 = str(input("NOME DO ALUNO 3: "))
a4 = str(input("NOME DO ALUNO 4: "))
lista = [a1, a2, a3, a4]


print(" O ALUNO ESCOLHIDO FOI: {}".format(random.choice(lista)))






