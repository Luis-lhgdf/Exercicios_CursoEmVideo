# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções
# incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa
# que importe esse módulo e use algumas dessas funções.

def aumentar(valor=0, taxa=0, formato=False):
    ret = valor + (taxa * valor / 100)
    return ret if formato is False else moeda(ret)


def diminuir(valor=0, desconto=0, formato=False):
    ret = valor - (desconto * valor / 100)
    return ret if formato is False else moeda(ret)


def dobro(valor=0, formato=False):
    ret = valor * 2
    return ret if formato is False else moeda(ret)


def metade(valor=0, formato=False):
    ret = valor / 2
    return ret if formato is False else moeda(ret)


def moeda(valor=float(0), tipoMoeda="R$"):
    return f'{tipoMoeda}{valor:.2f}'.replace(".", ",")


def resumo(valor=0, taxa=0, desconto=0, formato=False):
    print(f"-="*40)
    print(f"{'RESUMO DO VALOR':^40},{valor}")
    print(f"-=" * 40)
    print(f"O dobro de {moeda(valor)} é: {dobro(valor, formato)}")
    print(f"A metade de {moeda(valor)} é: {metade(valor, formato)}")
    print(f"O valor atual de {moeda(valor)} passa ser: {aumentar(valor, taxa, formato)} com a taxa de {taxa}%")
    print(f"O valor atual de {moeda(valor)} passa ser: {diminuir(valor, desconto, formato)} com o desconto de {desconto}%")
    print(f"-=" * 40)
