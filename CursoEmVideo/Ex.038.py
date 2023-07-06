# Exercício Python 038: escreva um programa que leia dois números inteiros e compare-os. Mostrando uma mensagem na tela:
# — O primeiro valor é maior

# – O segundo valor é maior

# – Não existe valor maior, os dois são iguais

a = float(input("DIGITE O PRIMEIRO VALOR: "))
b = float(input("DIGITE O SEGUNDO VALOR: "))

if a == b:
    print("NÃO EXISTE VALOR DIFERENTES AMBOS SÃO IGUAIS! ")
elif a>b:
    print("O PRIMEIRO VALOR {} É O MAIOR!".format(a))
elif b>a:
    print("O SEGUNDO VALOR {} É O MAIOR".format(b))
else:
    print("valor invalido")



