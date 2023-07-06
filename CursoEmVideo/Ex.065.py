# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
lista = []
maior = menor = 0
resp = "S"
cont = 0
soma = 0
while resp =="S":
    nun = int(input("DIGITE UM VALOR: "))
    lista.append(nun)
    cont +=1
    soma += nun
    resp = str(input("GOSTARIA DE CONTINUAR? [S/N]: ")).strip().upper()[0]
    if resp not in "N,S":
        print(40 * "_")
        print("""   INFORME UMA RESPOSTA VALIDA!
    PROGRAMA FINALIZADO""")

print(40*"_")
print(f"OS VALORES ESCOLHIDOS FORAM {lista}")
print(40*"_")

print("A MEDIA ENTRE ELES É {:.2f}\nSENDO O MAIOR {}\nE O MENOR {}".format(soma/cont, max(lista), min(lista)))
print(40*"_")
