# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = list()
for c in range(0, 5):
    valores.append(int(input(f"DIGITE O {c+1}° VALOR PARA A POSIÇÃO {c}: ")))
maior = max(valores)
menor = min(valores)
print(f"O MAIOR VALOR É {maior} E SUA POSIÇÃO É: ", end="")
for i, v in enumerate(valores):
    if v == maior:
        print(i, end=" ")
print()
print(f"O MENOR VALOR É {menor} E SUA POSIÇÃO É: ", end="")
for i, v in enumerate(valores):
    if v == menor:
        print(i, end=" ")
