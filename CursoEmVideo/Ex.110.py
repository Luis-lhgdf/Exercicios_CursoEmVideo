# Exercício Python 110: adicione o módulo moeda.py criado nos desafios anteriores,
# uma função chamada resumo(), que mostre na tela algumas informações geradas pelas
# funções que já temos no módulo criado até aqui.
from modulos import moeda

resp = float(input("DIGITE O VALOR: "))
moeda.resumo(resp, 50, 50, formato=True)
