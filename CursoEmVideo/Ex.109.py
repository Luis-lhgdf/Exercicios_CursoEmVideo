# Exercício Python 109: modifique as funções criadas no desafio 107
# para elas aceitarem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda()
# desenvolvida no desafio 108.
from modulos import moeda

resp = float(input("DIGITE O VALOR: "))
print(f"O dobro de {moeda.moeda(resp)} é: {moeda.dobro(resp,True)}")
print(f"A metade de {moeda.moeda(resp)} é: {moeda.metade(resp,True)}")
print(f"O valor atual de {moeda.moeda(resp)} passa ser: {moeda.aumentar(resp, 10,True)} com a taxa de 10%")
print(f"O valor atual de {moeda.moeda(resp)} passa ser: {moeda.diminuir(resp, 20,True)} com o desconto de 20%")
