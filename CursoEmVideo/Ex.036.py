# Exercício Python 36: escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

imovel = int(input("QUAL O VALOR DO IMÓVEL? R$"))
salario = int(input("QUAL O SEU SALARIO BRUTO ATUALMENTE? R$"))
anos = int(input("EM QUANTOS ANOS VOCE GOSTARIA DE QUITAR O SEU IMOVEL? "))

porcent = 30 * salario / 100
meses = anos * 12
pmensal = imovel / meses

if pmensal > porcent:
    print("INFELIZMENTE VOCE NÃO PODERA ADQUIRIR ESTE IMOVEL POIS ULTRAPASSA A NOSSA CONDIÇÃO DE 30%")
else:
    print("MEUS PARABENS, SEU EMPRÉSTIMO FOI APROVADO, SEGUE AS INFORMAÇÕES DO SEU CONTRATO:")
    print("SEU IMOVEL CUSTARA R${:.2f}, COM PARCELAS DE R${:.2f} EM {}X SEM JURUS".format(imovel, pmensal, meses))


