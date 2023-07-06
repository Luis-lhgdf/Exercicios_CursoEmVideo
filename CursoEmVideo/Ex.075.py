# Exercício Python 075. Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


nun = (int(input("DIGITE O 1° VALOR: ")), int(input("DIGITE O 2° VALOR: ")), int(input("DIGITE O 3° VALOR: ")), int(input("DIGITE O 4° VALOR: ")))

print("O NUMERO 9 APARECEU {}x".format(nun.count(9)))
if 3 in nun:
    print("O NUMERO 3 ESTA NA {}° POSIÇÃO".format(nun.index(3) + 1))
    print("OS NUMEROS PARES SÃO OS: ", end="")
else:
    print("O VALOR DE NUMERO 3 NAO FOI DIGITADO PELO USUÁRIO!")
    print("OS NUMEROS PARES SÃO OS: ", end="")
for n in nun:
    if n % 2 == 0:

        print(f"{n}", end=" ")


