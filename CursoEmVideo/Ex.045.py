# Exercício Python 45. Crie um programa que faça o computador jogar Jokenpô com você.
import emoji
import random

stone = (emoji.emojize("\U0001f44a "))
paper = (emoji.emojize("\U0001f590\uFE0F "))
scissors = (emoji.emojize("\u270C\uFE0F "))
jukenpo = ["PEDRA", "PAPEL", "TESOURA"]
pc = random.choice(jukenpo)

print(21 * "\033[1;31m=-\033[m", "\n            \033[1;33mGAME OF JOKENPO\033[m         \n", 20 * "\033[1;31m=-\033[m")


# AGUARDANDO ESCOLHA DO PLAYER:
player = str(input("PEDRA, PAPEL OU TESOURA? ")).upper().strip()

# CASO O PLAYER ESCOLHA PEDRA:
if player == "PEDRA":
    print(20*"_")
    print("PEDRA" + " X " + pc)
    if pc == "PEDRA":
        print(stone + "   X   " + stone)
        print(20 * "_")
        print("EMPATOU")
    elif pc == "TESOURA":

        print(stone + "   X   " + scissors)
        print(20 * "_")
        print("\033[1;34m MUITO BEM, VOCÊ GANHOU!!!\033[m")
    elif pc == "PAPEL":

        print(stone + "   X   " + paper)
        print(20 * "_")
        print("\033[1;31mVOCE PERDEU:(\033[m")

# CASO O PLAYER ESCOLHA TESOURA:
if player == "TESOURA":
    print(20 * "_")
    print("TESOURA" + " X " + pc)
    if pc == "TESOURA":
        print("  ", scissors + "X  " + scissors)
        print(20 * "_")
        print("EMPATOU")
    elif pc == "PEDRA":

        print("  ",scissors + "X   " + stone)
        print(20 * "_")
        print("\033[1;31mVOCE PERDEU:(\033[m")
    elif pc == "PAPEL":

        print("  ",scissors + "X   " + paper)
        print(20 * "_")
        print("\033[1;34m MUITO BEM, VOCÊ GANHOU!!!\033[m")

# CASO O PLAYER ESCOLHA PAPEL:
if player == "PAPEL":
    print(20 * "_")
    print("PAPEL" + " X " + pc)
    if pc == "PAPEL":
        print(20 * "_")
        print(paper + "   X   " + paper)
        print(20 * "_")
        print("EMPATOU")
    elif pc == "PEDRA":

        print(paper + "   X   " + stone)
        print(20 * "_")
        print("\033[1;34m MUITO BEM, VOCÊ GANHOU!!!\033[m")
    elif pc == "TESOURA":

        print(paper + "   X   " + scissors)
        print(20 * "_")
        print("\033[1;31mVOCE PERDEU:(\033[m")
else:
    print("")
    print("")
    print("TENTE NOVAMENTE")
