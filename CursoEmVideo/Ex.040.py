# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, conforme a média atingida:

# – Média abaixo de 5.0: REPROVADO

# – Média entre 5,0 e 6,9: RECUPERAÇÃO

# – Média 7.0 ou superior: APROVADO

n1 = float(input("DIGITE SUA 1° NOTA: "))
n2 = float(input("DIGITE SUA 2° NOTA: "))
m = (n1 + n2) / 2

if m >= 7:
    print("VOCE FOI APROVADO COM A MÉDIA {}".format(m))
elif m <=5:
    print("VOCE FOI REPROVADO COM A MÉDIA {}".format(m))
else:
    print("VOCE ESTA EM RECUPERAÇÃO POR TER FICADO COM A MÉDIA {}".format(m))
