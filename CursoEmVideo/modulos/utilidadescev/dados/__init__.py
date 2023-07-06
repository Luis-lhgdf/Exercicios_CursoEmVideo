# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111,
# temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
# que seja capaz de funcionar como a função imputa(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.


def leiaDinheiro(msg):
    valido = False
    while not valido:
        nun = str(input(msg)).strip().replace(",", ".")
        if nun.isalpha() or len(nun) == 0:
            print(f'\033[31mERRO: \"{nun}\" É UM VALOR INVALIDO!\033[m')
        else:
            valido = True
            return float(nun)


def leiaint(msg="digite um valor int: "):
    while True:
        try:
            nun = int(input(msg))
        except Exception as erro:
            print(f"HOUVE UM ERRO DE --> \033[31m{erro}\033[m <---, TENTE NOVAMENTE:")
            continue
        else:
            return nun


def leiafloat(msg):
    while True:
        try:
            nun = float(input(msg))
        except Exception as erro:
            print(f"HOUVE UM ERRO DE --> \033[31m{erro}\033[m <---, TENTE NOVAMENTE:")
            continue
        else:
            return nun


def leiaNome(msg):
    try:
        nome = str(input(msg).strip().capitalize())
        while len(nome) <=0 or not nome.isalpha():
            print("Valor invalido, digite novamente: ")
            nome = str(input(msg).strip().capitalize())
    except Exception as erro:
        print(f"Houve um erro ao adicionar o nome: {erro} ")
    else:
        return nome
