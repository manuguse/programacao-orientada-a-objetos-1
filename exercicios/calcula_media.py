"""- Considerar uma turma da Disciplina de Cálculo I, com 5 alunos, fazer um programa que tenha uma . 
    Esta função deve retornar a média da turma e a nota do aluno com a média mais alta.
    
    função que calcule a média das notas da turma e verifique o aluno com a melhor nota
    

No programa principal após conhecer o média mais alta, informe seu status (aprovado, reprovado ou em recuperação).
Para definir o status assuma a seguinte premissa: Considerando que essas regras funcionam da mesma forma que funcionam na UFSC:
se a média for 5.75 ou maior, o aluno está aprovado, se o aluno não estiver aprovado mas a nota for maior ou igual a 2.75,
ele tem o direito de fazer a prova de recuperação e se a média for menor que 2.75 ele está reprovado."""

def mensagem_final(media, melhorNota, status):
    print(f'\nmédia turma: {media:.2f}')
    print(f'melhor aluno: {melhorNota:.2f} | status: {status}')
    
def calcula_media():
    somaNota = 0
    melhorNota = 0
    for i in range(5):
        while True:
            nota = float(input('insira a nota '))
            if 0 <= nota <= 10:
                break
            print('nota invalida')
        somaNota += int(nota)
        if nota > melhorNota:
            melhorNota = nota
    media = (somaNota/5)
    status = verifica_aprovacao(melhorNota)
    return media, melhorNota, status
    
def verifica_aprovacao(melhorNota): 
    if melhorNota < 2.75:
        status = 'reprovado'
    elif melhorNota < 5.75:
        status = 'recuperacao'
    else:
        status = 'aprovado'
    return status
        
media, melhorNota, status = calcula_media()
mensagem_final(media, melhorNota, status)
