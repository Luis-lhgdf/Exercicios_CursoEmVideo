# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input("INFORME O VALOR DO PRODUTO: "))
d = (5*p)/100
print("O PRODUTO GANHOU UM DESCONTO DE 5%, O VALOR PASSAR SER AGORA {}R$!!!".format(p-d))


