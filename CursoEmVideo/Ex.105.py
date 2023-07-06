# Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# – Quantidade de notas
# — A maior nota
# — A menor nota
# — A média da turma
# — A situação (opcional)
def notas(*nota, situacao=False):
    notas_alunos = []
    media_turma = 0
    for n in nota:
        notas_alunos.append(n)
    for n in notas_alunos:
        media_turma +=n
    media_turma = media_turma/len(notas_alunos)
    maior_nota = max(notas_alunos)
    menor_nota = min(notas_alunos)
    print(f"AS NOTAS FORAM: {notas_alunos}\n"
          f"A MENOR NOTA FOI: {menor_nota}\n"
          f"A MAIOR NOTA FOI> {maior_nota}\n"
          f"A MEDIA DA TURMA FOI: {media_turma}")
    if situacao:
        if media_turma <=4:
            situacao_final = "RUIN"
        elif 5 <= media_turma <= 7:
            situacao_final = "REGULAR"
        else:
            situacao_final = "BOA"
        print(f"A SITUAÇÃO FINAL FOI: {situacao_final}")


notas(5,4,3,2,1, situacao=True)