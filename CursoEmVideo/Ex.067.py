# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
print(f"{'GERADOR DE TABUADAS':_^50}")
while True:
    nun = int(input("INFORME O VALOR QUE GOSTARIA DE SABER A SUA TABUADA: "))
    if nun >0:
        for c in range(1, 11, 1):
            print(f'{"~":~^12}')
            print(f"{nun} X {c} = {nun*c}")
    if nun <0:
        break
print(f'{"-":-^50}')
print("PROGRAMA ENCERRADO, OBRIGADO E VOLTE SEMPRE!!!")
print(f'{"-":-^50}')
