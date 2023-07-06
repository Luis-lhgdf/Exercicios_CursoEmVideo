# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
a = randint(1, 10)
nun = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print("OS VALORES GERADOS FORAM:{}\nSENDO O MAIOR: {}\nE O MENOR: {}".format(nun, max(nun), min(nun)))
