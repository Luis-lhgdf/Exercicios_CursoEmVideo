# Exercício Python 115a: Vamos criar um menu em Python, usando modularização
from modulos.utilidadescev.sistema import *
import time

if not arquivoExiste():
    criaArquivo("cadastro")

while True:
    resp = menu(["VER PESSOAS CADASTRADAS", "NOVO CADASTRO", "SAIR DO PROGRAMA", "EXCLUIR REGISTRO"])
    if resp == 1:

        cabecalho("OPÇÃO O1")
        visualizarArq('cadastro')

        time.sleep(2)
    elif resp == 2:

        cabecalho('OPÇÃO 02')
        n = leiaNome("DIGITE SEU NOME: ")
        i = leiaint("INFORME SUA IDADE: ")
        Cadastrar('cadastro', nome=n, idade=i)
    elif resp == 3:

        cabecalho("OPÇÃO 03")
        print("SAINDO DO PROGRAMA, ATÉ LOGO...")
        time.sleep(2)
        break

    elif resp == 4:
        cabecalho("OPÇÃO 04")

        resp = leiaint("INFORME O INDICES DA PESSOA QUE DESEJA REMOVER: ")
        exRegistro('cadastro', pos=resp)

    else:
        cabecalho("\033[31mRESPOSTA INVALIDA\033[m")
        time.sleep(1)
        resp = menu(["VER PESSOAS CADASTRADAS", "NOVO CADASTRO", "SAIR DO PROGRAMA"])
linha()
print("FIM".center(50))
linha()
