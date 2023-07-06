# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
geral = [[], []]
for c in range(0, 7):
    nun = int(input(f"DIGITE O {c+1}° VALOR: "))
    if nun % 2 == 0:
        geral[0].append(nun)
        geral[0].sort()
    elif nun % 2 != 0:
        geral[1].append(nun)
        geral[1].sort()
print(f"VALORES PARES: {geral[0]}\nVALORES IMPARES {geral[1]}")







