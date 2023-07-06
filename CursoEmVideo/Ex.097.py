# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável
# escreva(‘Olá, Mundo!’) Saída:

# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def escreva(text):
    t = len(text) + 5
    print("~" * t)
    print(f"{text:^{t}}")
    print("~" * t)


escreva("luis henrique gomes da fonseca")
