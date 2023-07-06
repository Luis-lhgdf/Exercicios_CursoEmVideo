# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível
# pelo computador usado.
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except Exception as erro:
    print(f"houve um erro de {erro}")
else:
    print("acessado com sucesso")
