# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ("amor", "caderno", "cachorro", "lampada", "livro", "chinelo", "mouse", "teclado")

for p in palavras:
    print(f"\nNA PALAVRA \033[1;34m{p.upper()}\033[m TEMOS ESSAS VOGAIS: ", end="")
    for l in p:
        if l.lower().strip() in "aeiou":
            print(f"\033[1;33m{l.upper()}\033[m", end=" ")

