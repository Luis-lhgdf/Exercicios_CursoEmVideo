# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.
value = ""

while len(value) <=0:
    value = str(input("digite qualquer valor: ").strip())
else:
    print(f"{value.isalnum()}")
    print(f"{value.isalpha()}")
