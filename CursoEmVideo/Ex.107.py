# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções
# incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa
# que importe esse módulo e use algumas dessas funções.

from modulos import moeda

resp = float(input("DIGITE O VALOR: R$"))
print(f"O dobro de R${resp} é: R${moeda.dobro(resp)}")
print(f"A metade de R${resp} é: R${moeda.metade(resp)}")
print(f"O valor atual de R${resp} passa ser: R${moeda.aumentar(resp, 10)} com a taxa de 10%")
print(f"O valor atual de R${resp} passa ser: R${moeda.diminuir(resp, 20)} com o desconto de 20%")
