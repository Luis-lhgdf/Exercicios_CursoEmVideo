# Exercício Python 31. Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200Km e R$0,45 parta viagens mais longas.

print(20*">=")
print("    CALCULE O VALOR DE SUA PASSAGEM")
print(20*">=")
v = float(input("DIGITE A DISTANCIA DE SUA VIAGEM: KM "))
if v <= 200:
    print(" ")
    print("SUA VIAGEM É DE {}KM E VOCE DEVERA PAGAR R${} PARA A NOSSA COMPANHIA.".format(v, v * 0.50))
else:
    print(" ")
    print("SUA VIAGEM É DE {}KM E VOCE DEVERA PAGAR R${} PARA A NOSSA COMPANHIA.".format(v, v * 0.45))

print(" ")
print(" ")

print(" ")
print(" ")
print(" ")
print(30*">=")
print("    OBRIGADO POR USAR NOSSOS SERVIÇOS, VOLTE SEMPRE")
print(30*">=")

