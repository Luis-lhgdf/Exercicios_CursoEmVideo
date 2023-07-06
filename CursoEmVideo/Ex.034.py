# Exercício Python 34: escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input("DIGITE O SEU SALARIO: R$ "))
if s > 1250:
    print("VOCÊ RECEBE {} E GANHARA UM AUMENTO DE 10%, SEU NOVO SALARIO É R${}".format(s, (10*s/100)+s,))
else:
    print("VOCE RECEBE {} E GANHARA UM AUMENTO DE 15%, SEU NOVO SALARIO É R${}".format(s, (15*s/100)+s))


