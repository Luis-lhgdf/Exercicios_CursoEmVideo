# Exercício Python 37: escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

nun = int(input("DIGITE UM VALOR INTEIRO: "))
print("ESCOLHA QUAL SERA A BASE DE CONVERSÃO:")
print("\033[1;31mDIGITE 1 PARA BINARIO\033[m >>>>>>> \033[1;32mDIGITE 2 PARA OCTAL\033[m >>>>>> \033[1;34mDIGITE 3 PARA HEXADECIMAL\033[m)")
escolha = int(input("QUAL CONVERSÃO DESEJA?  "))

if escolha == 1:
    print("\033[1;31mA CONVERSÃO DE {} PARA VALOR BINARIO FICA {}\033[m".format(nun, bin(nun)))
elif escolha == 2:
    print("\033[1;32A CONVERSÃO DE {} PARA VALOR OCTAL FICA {}\033[m".format(nun, oct(nun)))
elif escolha == 3:
    print("\033[1;34mA CONVERSÃO DE {} PARA VALOR HEXADECIMAL FICA {}\033[m".format(nun, hex(nun)))
else:
    print("VALOR INVALIDO, TENTE NOVAMENTE")
    nun = int(input("DIGITE UM VALOR INTEIRO: "))
    print("ESCOLHA QUAL SERA A BASE DE CONVERSÃO:")
    print("\033[1;31mDIGITE 1 PARA BINARIO\033[m >>>>>>> \033[1;32mDIGITE 2 PARA OCTAL\033[m >>>>>> \033[1;34mDIGITE 3 PARA HEXADECIMAL\033[m)")
    escolha = int(input("QUAL CONVERSÃO DESEJA?  "))
if escolha == 1:
    print("\033[1;31mA CONVERSÃO DE {} PARA VALOR BINARIO FICA {}\033[m".format(nun, bin(nun)))
elif escolha == 2:
    print("\033[1;32A CONVERSÃO DE {} PARA VALOR OCTAL FICA {}\033[m".format(nun, oct(nun)))
elif escolha == 3:
    print("\033[1;34mA CONVERSÃO DE {} PARA VALOR HEXADECIMAL FICA {}\033[m".format(nun, hex(nun)))


print("FIM")
