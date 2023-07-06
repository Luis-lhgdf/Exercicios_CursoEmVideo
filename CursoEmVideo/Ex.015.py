# Exercício Python 15: escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
# R$0,15 por km rodado.
km = int(input("INFORME A QUILOMETRAGEM PERCORRIDA NO PERIODO ALUGADO: "))
d = int(input("INFORME AGORA, QUANTOS DIAS VOCE PERCORREU COM O VEICULO ALUGADO: "))

t2 = (km*0.15)+(d*60)

print("O VALOR TOTAL A PAGAR É DE R${}".format(t2))
