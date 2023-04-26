def verificaAdicao():
    while True:
        x = input('deseja adicionar alguem? ').upper()
        if x == 'S' or x == 'N':
            break
    return x

def verificaModalidade():
    while True:
        x = input('escolha a modalidade (f/n/v/b) ').lower()
        if x == 'f' or x == 'n' or x == 'v' or x == 'b':
            break
    return x

def insereAluno():
    x = input('insira o nome do aluno ')
    return x

def verificaRepetido(k, j):
    y = []
    if k.isdisjoint(j) == False:
        y = repetidos.append(k.intersection(j))
    return y

futebol = {'maria', 'joao', 'pedro'}
natacao = {'vitor', 'maria', 'jorge'}
volei = {'mario', 'jaime', 'clara'}
basquete = {'joao', 'ana', 'paulo'}

print(f'alunos futebol: {futebol}')
print(f'alunos natacao: {natacao}')
print(f'alunos volei: {volei}')
print(f'alunos basquete: {basquete}')

while True:
    adicionar = verificaAdicao()
    if adicionar == 'N':
        break
    else:
        modalidade = verificaModalidade()
        if modalidade == 'f':
            futebol.add(insereAluno())
        elif modalidade == 'n':
            natacao.add(insereAluno())
        elif modalidade == 'v':
            volei.add(insereAluno())
        elif modalidade == 'b':
            basquete.add(insereAluno())

repetidos = []

verificaRepetido(futebol, natacao)
verificaRepetido(futebol, volei)
verificaRepetido(futebol, basquete)
verificaRepetido(volei, natacao)
verificaRepetido(natacao, basquete)
verificaRepetido(volei, basquete)

alunosTotal = (futebol | natacao | volei | basquete) 

print(f'alunos com desconto: {repetidos}')
print(f'qtde alunos futebol: {len(futebol)}')
print(f'qtde alunos natacao: {len(natacao)}')
print(f'qtde alunos volei: {len(volei)}')
print(f'qtde alunos basquete: {len(basquete)}')
print(f'qtde alunos total: {len(alunosTotal)}')
