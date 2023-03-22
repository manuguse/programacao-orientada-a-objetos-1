"""Considerar uma turma da Disciplina de Cálculo I, com 5 alunos, fazer um programa que:
    - Calcule a média das notas;
    - Indique o nome do aluno com a média mais alta
    - Considerando o aluno com a nota mais alta, informe seu conceito (Aprovado, Em Recuperação, Reprovado). 
      Considerando que essas regras funcionam da mesma forma que na UFSC: se a média for 5.75 ou maior, o aluno
      está aprovado, se a nota for maior ou igual a 2.75, ele tem o direito de fazer a prova de recuperação e
      se o aluno obtiver uma média menor que 2.75 ele foi reprovado."""

somaNotas = 0

for i in range (5):
    aluno = input('nome aluno ')
    nota = float(input('nota aluno '))
    somaNotas += nota
    
    if (i == 0):
        melhorAluno = aluno
        melhorNota = nota
    elif (nota > melhorNota):
        melhorAluno = aluno
        melhorNota = nota

if (melhorNota >= 5.75):
    situacao = 'aprovado'
elif (melhorNota >= 2.75):
    situacao = 'em recuperação'
else:
    situacao = 'reprovado'

print(f'média das notas: {somaNotas/5}')
print(f'melhor média: {melhorAluno}')
print(f'situação: {situacao}')
