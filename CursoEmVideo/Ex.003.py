# Exercício Python 3: Crie um programa que leia dois números e mostre a soma entre eles.

nun = []
for c in range(0, 2):
    try:
        nun.append(int(input(f"digite o {c + 1}° valor: ")))
    except Exception as erro:
        print(f"ocorreu um erro de {erro}")
        break
if len(nun) <=1:
    print("fim")
else:
    print(f'{nun} = {sum(nun)}')
    print("fim")
