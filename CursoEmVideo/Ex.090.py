# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
pessoas = {"Nome": str(input("DIGITE SEU NOME: ")).strip().capitalize(), "Media": int(input("DIGITE SUA MÉDIA: "))}
if 5 <= pessoas["Media"] <= 6:
    pessoas["Situação"] = "Recuperação"
if 0 <= pessoas["Media"] <= 4:
    pessoas["Situação"] = "Reprovado"
if 7 <= pessoas["Media"] <= 10:
    pessoas["Situação"] = "Aprovado"
for k, v in pessoas.items():
    print(f"{k} é igual a {v}")


