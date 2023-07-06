from modulos.utilidadescev.dados import *


def linha(xlinha=50):
    print("-" * xlinha)


def cabecalho(title):
    linha()
    print(f"\033[35m{title}\033[m".center(60))
    linha()


def menu(lista_de_op):
    cabecalho('MENU PRINCIPAL')
    for i, v in enumerate(lista_de_op):
        print(f"{i + 1:.<5}{v:<40}")
    linha()
    escolha = leiaint("\033[32mSUA OPÇÃO: \033[m")
    return escolha


def lista_de_ops(title, lista):
    cabecalho(title)
    for i, v in enumerate(lista):
        print(f"{i + 1:.<5}{v:<40}")
    linha()
    escolha = leiaint("\033[32mSUA OPÇÃO: \033[m")
    return escolha


def arquivoExiste(name="cadastro"):
    try:
        arq = open(name, "rt")
        arq.close()
    except FileNotFoundError:
        print(f"arquivo {name} nao foi encontrado")
        return False
    else:
        return True


def criaArquivo(name):
    try:
        arq = open(name, 'wt+')
        arq.close()
    except Exception as erro:
        print(f"Houve algum erro ao tentar criar o arquivo {erro}")
    else:
        print(f"ARQUIVO {name} CRIADO COM SUCESSO")


def visualizarArq(arq):
    try:
        arquivo = open(arq, "rt")

    except Exception as erro:
        print(f"Houve um erro ao visualizar as pessoas cadastradas, {erro}")
    else:
        for i, l in enumerate(arquivo):
            dado = l.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{i + 1} {dado[0]:.<35}{dado[1]:.3} Anos")
        arquivo.close()


def Cadastrar(arq, nome="Desconhecido", idade=0):
    try:
        arquivo = open(arq, "at")
    except Exception as erro:
        print(f"Houve algum erro ao abrir o arquivo para adicionar uma nova pessoa {erro}")
    else:
        try:
            arquivo.write(f"{nome};{idade}\n")
        except Exception as erro:
            print(f"houve um erro ao adicionar uma pessoa {erro}")
        else:
            print(f"{nome} foi adicionado com sucesso")
            arquivo.close()


def exRegistro(arq, pos):
    # Abre o arquivo em modo de leitura
    with open(arq, "r") as file:
        # Lê as linhas do arquivo e armazena em uma lista
        lines = file.readlines()

    # Pede ao usuário a linha a ser excluída
    line_to_delete = pos

    # Verifica se a linha informada existe no arquivo
    if line_to_delete > len(lines):
        print("Linha inválida.")
    else:
        # Remove a linha informada da lista
        lines.pop(line_to_delete - 1)

    # Abre o arquivo em modo de escrita
    with open(arq, "w") as file:
        # Grava as linhas restantes no arquivo
        file.writelines(lines)

    print("Linha excluída com sucesso.")
