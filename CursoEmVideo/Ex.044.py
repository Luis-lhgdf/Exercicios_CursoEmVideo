# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

produto = float(input("QUAL O VALOR DO PRODUTO:  R$"))
print("""DIGITE O NUMERO REFERENTE A CONDIÇÃO DE PAGAMENTO: 
\033[1;31m[1] à vista dinheiro/cheque\033[m
\033[1;32m[2] à vista no cartão\033[m
\033[1;33m[3] em até 2x no cartão:\033[m 
\033[1;34m[4] 3x ou mais no cartão\033[m""")
condp = int(input("INFORME  O NUMERO DE UMA DAS OPÇÕES ACIMA: "))

if condp == 1:
    print("SEU PRODUTO CUSTA R${} E COM ESTA CONDIÇÃO DE PAGAMENTO PASSARA A SER R${} COM O DESCONTO APLICADO ".format(produto, produto - (10*produto/100)))
elif condp == 2:
    print("SEU PRODUTO CUSTA R${} E COM ESTA CONDIÇÃO DE PAGAMENTO PASSARA A SER R${}  COM O DESCONTO APLICADO".format(produto, produto - (5*produto/100)))
elif condp == 3:
    print("SEU PRODUTO CUSTA R${} POREM ESTA CONDIÇÃO DE PAGAMENTO NÃO LHE FORNECE DESCONTO ".format(produto))
elif condp == 4:
    print("SEU PRODUTO CUSTA R${} E COM ESTA CONDIÇÃO DE PAGAMENTO PASSARA A SER R${} COM O JUROS APLICADO".format(produto, produto + (20*produto/100)))

else:
    print("ERROR")