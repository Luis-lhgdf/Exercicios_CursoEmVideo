# Exercício Python 61: refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
final = 10
cont = 0
inic = int(input("DIGITE O PRIMEIRO TERMO: "))
pulando = int(input("DIGITE A RAZÃO: "))
while cont < final:
    print(inic, end=" -> ")

    inic += pulando
    cont +=1
print("fim")

