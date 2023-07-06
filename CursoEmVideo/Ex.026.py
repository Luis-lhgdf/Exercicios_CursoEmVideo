# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("DIGITE UMA FRASE: ")).strip().upper()

print("A PRIMEIRA VEZ QUE APARECE A LETRA 'A' É NA POSIÇÃO {} E A ULTIMA NA POSIÇÃO {}".format(frase.find("A")+1, frase.rfind("A")+1))
print("A LETRA 'A' APARECE {}X".format(frase.count("A")))

