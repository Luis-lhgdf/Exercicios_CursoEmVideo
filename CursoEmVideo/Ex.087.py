# Crie um programa que declare uma matriz de dimensão 3×3
# e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
# Aprimore o desafio mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma3c = maior2l = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"DIGITE OS VALORES PARA A MATRIZ [{l}, {c}]: "))
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        print(f"[{matriz[l][c]:^5}]", end="")
    print()
for c in range(0, 3):
    soma3c += matriz[c][2]
maior2l = max(matriz[1])
print(f"A soma de todos os valores pares digitados é {somapar}.")
print(f"A soma dos valores da terceira coluna é {soma3c}.")
print(f"O maior valor da segunda linha é {maior2l}.")
