# Exercício Python 49: refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

nun = int(input("DIGITE UM VALOR PARA RETORNAR SUA TABUADA: "))
for c in range(0, 11, 1):
    print("{} X {} = {}".format(nun, c, nun*c))
