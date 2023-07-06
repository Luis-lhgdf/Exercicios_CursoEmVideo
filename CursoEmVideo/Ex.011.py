# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
l = float(input("INFORME A LARGURA DA PAREDE: "))
a = float(input("INFORME A ALTURA DA PAREDE: "))
ar = l*a
print(" SUA PAREDE TEM {}M² E VOCE PRECISARA DE {:.2f} LITROS DE TINTA PARA PINTALA POR COMPLETA!!! ".format(ar, ar/2))


