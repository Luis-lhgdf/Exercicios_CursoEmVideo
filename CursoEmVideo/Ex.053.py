# Exercício Python 53: crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:

# APOS A SOPA,
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA.

frase = str(input("DIGITE UM FRASE: ")).strip().upper()
separada = frase.split()
junto = "".join(separada)
inverso = junto[::-1]
if junto == inverso:
    print("ELA É UM PALINDROMO")
else:
    print("ELA NÃO É UM PALINDROMO")
print("A FRASE {} INVERTIDA FICA {} ".format(junto, inverso))

