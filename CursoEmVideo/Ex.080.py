# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""lista = []

for c in range(0, 5):
    valor = int(input("DIGITE UM VALOR: "))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print("valor adicionado ao final da lista")
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos,valor)
                print(f"valor adicionado na posição {pos}")
                break
            pos +=1
print(lista)"""
lista = []

for c in range(0, 5):
    valor = int(input("DIGITE UM VALOR: "))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print("valor adicionado ao final da lista")
        print(lista)
    else:
        if valor <= lista[0]:
            lista.insert(0, valor)
            print("valor adicionadona posição 0")
            print(lista)

        elif valor <= lista[1]:
            lista.insert(1, valor)
            print("valor adicionadona posição 1")
            print(lista)

        elif valor <= lista[2]:
            lista.insert(2, valor)
            print("valor adicionadona posição 2")
            print(lista)

        elif valor <= lista[3]:
            lista.insert(3, valor)
            print("valor adicionadona posição 3")
            print(lista)

        elif valor <= lista[4]:
            lista.insert(4, valor)
            print("valor adicionadona posição 4")
            print(lista)
print(f"lista final {lista}")
