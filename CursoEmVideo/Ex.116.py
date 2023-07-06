from modulos.utilidadescev.dados import *


def arquivoExiste(name_arq=""):
    try:
        with open(name_arq, "r") as arquivo:
            print(f"ARQUIVO '{arquivo.name}' ENCONTRADO COM SUCESSO!!")
            return True
    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO :(")
        return False
    except Exception as erro:
        print(f"ERRO {erro}")


def criarArquivo(name_arq=""):
    verificar = arquivoExiste(name_arq)
    if not verificar:
        with open(name_arq, "w+") as arquivo:
            print(F"ARQUIVO '{arquivo.name}' CRIADO COM SUCESSO!!!")
    else:
        print(f"ARQUIVO COM O NOME '{name_arq} JA EXISTE'")


def excluirArquivo(name_arq=""):
    import os
    verificar = arquivoExiste(name_arq)
    if verificar:
        os.remove(name_arq)
        print(f"ARQUIVO{name_arq} FOI REMOVIDO COM SUCESSO")


def excluirLinha(name_arq):
    while True:
        try:
            with open(name_arq, "r") as arquivo:
                copia = arquivo.readlines()
                copia.pop(leiaint("informe o indice que deseja excluir: ") - 1)
        except FileNotFoundError:
            print("Arquivo não existe, informe um arquivo existente!")
            break
        except IndexError:
            print("A LINHA INFORMADA NÃO EXISTE")
            continue
        else:

            with open(name_arq, "w") as arquivo:
                arquivo.writelines(copia)
                print("LINHA REMOVIDA COM SUCESSO!!!")
                break


def add_newline(name_arq, msg_input=""):
    try:
        with open(name_arq, 'a') as arquivo:
            txt = str(input(msg_input).strip())
            arquivo.write(f'{txt}\n')
    except FileNotFoundError:
        print("Arquivo não encontrado")
    else:
        print(f"linha {txt} - adicionada com sucesso!!!")


def editarRegistro(name_arq, line_number=0, new_text=""):
    # Abrir o arquivo em modo leitura
    with open(name_arq, 'r') as file:
        # Lê todas as linhas do arquivo e armazena em uma lista
        lines = file.readlines()

    # Substitui a linha especificada pelo usuário pelo novo texto
    lines[line_number - 1] = new_text + '\n'

    # Abrir o arquivo em modo escrita
    with open(name_arq, 'w') as file:
        # Escrever todas as linhas de volta ao arquivo
        file.writelines(lines)

