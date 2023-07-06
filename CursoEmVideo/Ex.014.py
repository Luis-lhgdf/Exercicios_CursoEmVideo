# Exercício Python 14: escreva um programa que converta uma temperatura digitando em graus Celsius e converta para
# graus Fahrenheit.

c = float(input("INFORME A TEMPERATURA EM GRAUS CELSIUS: "))
print("A CONVERSÃO FICA {}Celsius PARA {}FAHRENHEIT".format(c, (c*9/5)+32))
