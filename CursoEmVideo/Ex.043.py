# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, conforme a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida


altura = float(input("INFORME SUA ALTURA: M "))
peso = float(input("INFORME SEU PESO: KG "))
imc = peso / (altura ** 2)

if 0 <= imc < 18.5:
    print("SEU IMC É {:.2f} E VOCÊ ESTÁ ABAIXO DO PESO! ".format(imc))
elif 18.5 <= imc <=25:
    print("SEU IMC É {:.2f} E VOCÊ ESTÁ COM O PESO IDEAL! ".format(imc))
elif 25.5 <= imc <=30:
    print("SEU IMC É {:.2f} E VOCÊ ESTÁ COM SOBREPESO! ".format(imc))
else:
    print("SEU IMC É {:.2f} E VOCÊ ESTÁ COM OBESIDADE MÓRBIDA! ".format(imc))
