# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#
# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time da Chapecoense.


tabela = ("Palmeiras", "Internacional", "Fluminense",
          "Corinthians", "Flamengo", "Athletic Paranaense", "Atlético Mineiro", "Fortaleza", "São Paulo", "América",
          "Botafogo", "Santos", "Goiás", "Red Bull Bragantino", "Coritiba,"    "Cuiabá Saf", "Ceará", "Atlético",
          "Avaí", "Juventude")

while True:
    print("DIGITE [1] PARA AS INFORMAÇÕES DO BRASILEIRÃO\nDIGITE [2] PARA FECHAR O PROGRAMA")
    resp = int(input("SUA ESCOLHA [1] OU [2]: "))
    if resp not in (1, 2):
        resp = int(input("OPÇÃO INVALIDA, INFORME NOVAMENTE A SUA ESCOLHA [1] OU [2]: "))
    if resp == 2:
        break
    print(40*"-")
    print("OS 5 PRIMEIROS TIMES COLOCADOS FORAM {}".format(tabela[:5]))
    print("OS 4 ULTIMOS COLOCADOS FORAM {}".format(tabela[-4:]))
    print(f"SEGUE A BAIXO A LISTA DOS TIMES EM ORDEM ALFABÉTICA\n {sorted(tabela)}")
    resp2 = str(input("DIGITE O NOME DE ALGUM TIME PARA SABER A SUA POSIÇÃO NA TABELA: ")).strip().capitalize()
    if resp2 not in tabela:
        print("O TIME ESCOLHIDO NAO ESTA NA TABELA DO BRASILEIRÃO 2022")
        resp2 = str(input("DIGITE O NOME DE ALGUM TIME PARA SABER A SUA POSIÇÃO NA TABELA: ")).strip().capitalize()
    else:
        print("O {} ESTA NA {}° POSIÇÃO DA TABELA DO BRASILEIRÃO 2022".format(resp2, tabela.index(resp2)+1))

        break

