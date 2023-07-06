# Exercício Python 7: desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print("CALCULANDO A MÉDIA".center(50))
while True:
    try:
        n1 = float(input("DIGITE A SUA 1° NOTA: "))
        n2 = float(input("DIGITE A SUA 2° NOTA: "))
    except ValueError:
        print("\033[31m OCORREU UM ERRO\033[m")
    else:
        print(f'1° NOTA:{n1}\n2° NOTA: {n2}\nMÉDIA: {(n1+n2)/2}')
        break

