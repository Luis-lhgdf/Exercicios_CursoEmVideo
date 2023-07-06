# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
lista = ("PAPEL", 10, "TESOURA", 5, "CADERNO", 20, "LAPIS", 1.5)
for pos in range (0, len(lista)):
    if pos % 2 == 0:
        print(f"{lista[pos]:.<30}", end="")
    else:
        print("{}{:.2f}".format("R$", lista[pos]))