# uri 1547

def verificaQT():
    while True:
        qt = int(input('qtde de alunos '))
        if 4 <= qt <= 10:
            break
    return qt
    
def verificaSec():
    while True:
        sec = int(input('numero secreto '))
        if 1 <= sec <= 100:
            break
    return sec

n = int(input('numero de camisetas '))
qtLista = []

for i in range(n):
    vencedor = False
    qt = verificaQT()
    sec = verificaSec()
    for i in range(qt):
        qtLista.append(int(input(f'tentativa aluno {i + 1} ')))
    for i in range(qt):
        if qtLista[i] == sec:
            print(f'{i + 1}* aluno')
            vencedor = True
    while vencedor == False:
        for i in range(qt):
            cont = 1
            if qtLista[i] == (sec + cont) or qtLista[i] == (sec - cont):
                print(f'{i + 1}* aluno')
                vencedor = True
            cont += 1
    print('')
