# Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

while True:
    try:
        nun = int(input("DIGITE UM VALOR: "))
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")
        continue
    else:
        print(f"Voce escolheu o valor: {nun}\nSeu antecessor é:{nun - 1} E seu sucessor é: {nun + 1}")
        break
