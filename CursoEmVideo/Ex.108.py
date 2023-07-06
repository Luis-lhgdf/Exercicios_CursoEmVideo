# Exercício Python 108: adapte o código do desafio #107,
# criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

from modulos import moeda

resp = float(input("DIGITE O VALOR: "))
print(f"O dobro de {moeda.moeda(resp)} é: {moeda.moeda(moeda.dobro(resp))}")
print(f"A metade de {moeda.moeda(resp)} é: {moeda.moeda(moeda.metade(resp))}")
print(f"O valor atual de {moeda.moeda(resp)} passa ser: {moeda.moeda(moeda.aumentar(resp, 10))} com a taxa de 10%")
print(f"O valor atual de {moeda.moeda(resp)} passa ser: {moeda.moeda(moeda.diminuir(resp, 20))} com o desconto de 20%")
