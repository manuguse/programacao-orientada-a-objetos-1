"""1) Implemente um sistema que manipule as notas de n aluno(s). Cada aluno tem 3 Notas. Restrição de entrada: 0 <= Nota <= 10
O programa deve solicitar: o número de alunos da turma, o nome e as respectivas notas para cada aluno.
Ações esperadas:
    a) Indicar a média do aluno;
    b) Indicar a maior nota;
    c) Indicar a menor nota.
    d) Retorna a diferença entre a maior e a menor nota.
Considerar que não existem notas iguais."""

def verificaNota(nome, i, k):
    while True:
        x = float(input(f"insira a {k+1} nota de {nome[i]} "))
        if 0 <= x <= 10:
            break
    return x

nome = []
media = []
maiorNota = 0
menorNota = 10
maioresNotas = []
menoresNotas = []

num = int(input("numero de alunos "))
for i in range(num):
    nota = []
    somaNota = 0
    nome.append(input("insira o nome "))

    for k in range(3):
        nota.append(verificaNota(nome, i, k))
        somaNota += nota[k]
        if nota[k] > maiorNota:
            maiorNota = nota[k]
        if nota[k] < menorNota:
            menorNota = nota[k]

    media.append(somaNota/3)
    print(f"média de {nome[i]} = {media[i]:.2f}")
    
print(f"maior nota: {maiorNota}")
print(f"menor nota: {menorNota}")
print(f"diferença: {(maiorNota - menorNota):.2f}")
