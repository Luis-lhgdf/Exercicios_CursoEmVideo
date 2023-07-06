# Exercício Python 104: Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)


def leiaint(txt):
    user = input(f"{txt}").strip()
    verific = user.isnumeric()
    while not verific:
        print(f"\033[33m erro digite novamente\033[m")
        user = input(f"{txt}").strip()
        verific = user.isnumeric()

    print(f"voce acabou de digitar o numero {int(user)}")
    valor = int(user)
    return valor
teste = leiaint("digite um valor int: ")
print(teste)


