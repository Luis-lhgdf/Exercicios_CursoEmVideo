# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
inic = int(input("DIGITE O PRIMEIRO TERMO: "))
pulando = int(input("DIGITE A RAZÃO: "))
cont = 0
total = 0
mais = 10

while mais !=0:
    total = total + mais
    while cont <total:
        print(inic, " -> ", end="")
        inic += pulando
        cont +=1
    print("pausa")
    mais = int(input("\ngostaria de adicionar quantos termos a mais: "))
print("FIM")
