# Exercício Python 29: escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

print(20*">=")
print("        VERIFICADOR DE VELOCIDADE")
print(20*">=")
m = float(input("INFORME POR FAVOR EM QUAL VELOCIDADE VOCE ESTÁ: KM/H"))
if m > 80:
    print("VOCÊ FOI MULTADO! E DEVERA PAGAR O VALOR DE R${:.2f}".format((m-80)*7))
print("DIRIJA COM CUIDADO E ÓTIMA VIAGEM")
