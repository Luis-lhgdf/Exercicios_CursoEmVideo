# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial

nun = int(input("DIGITE UM VALOR: "))


def fatorial(valor, show=False):
    c = valor
    f = 1
    while c > 0:
        if show:
            print(f'{c}', end="")
            print(" x " if c > 1 else " = ", end="")
        f *= c
        c -= 1
    print(f"{f}")


help(fatorial)
