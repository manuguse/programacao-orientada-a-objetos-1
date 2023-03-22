"""3. Uma universidade particular oferece um desconto de 30% na mensalidade do aluno com melhor nota (média geral).
Implemente um programa que após receber as informações do aluno (nome, nota/média geral, valor mensalidade) verifique
quem é o aluno com melhor nota e calcule o desconto de sua mensalidade.

Ao final de sua execução, o programa deve mostrar:

- o nome do aluno com melhor nota,
- o valor da mensalidade (sem desconto)
- o valor da mensalidade com o desconto e 30%;

Considerar 5 alunos (as informações devem ser lidas do teclado), considerar alunos com notas distintas."""

for i in range (1,6):
    nome = str(input('nome '))
    nota = float(input('nota '))
    valor = float(input('valor '))
    
    if (i == 1):
        melhorNome = nome
        melhorNota = nota
        melhorValor = valor
    else:
        if (nota > melhorNota):
            melhorNome = nome
            melhorNota = nota
            melhorValor = valor

desconto = melhorValor*0.7
print(melhorNome)
print(melhorValor)
print(desconto)
