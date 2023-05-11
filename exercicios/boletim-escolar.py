def adiciona():
    while True:
        aluno = insereInfos()
        todosAlunos.append(aluno)
        continua = verificador("S", "N", False, "deseja continuar a adicionar? (S/N) ")
        if continua == "N":
            break

def consulta():
    while True:
        presente = False
        nome = input("insira o nome do aluno ")
        for i in range(len(todosAlunos)):
            if todosAlunos[i][0] == nome:
                presente = True
                print(f"nome: {todosAlunos[i][0]}")
                print(f"notas: {todosAlunos[i][1]}, {todosAlunos[i][2]}, {todosAlunos[i][3]}")
                print(f"media: {todosAlunos[i][4]:.2f}")
        if presente == False:
            print("o aluno nao foi adicionado ")
        continua = verificador("S", "N", False, "deseja continuar a consultar? (S/N) ")
        if continua == "N":
            break

def insereInfos():
    aluno = []
    soma = 0
    aluno.append(input("insira o nome "))
    for i in range(3):
        while True:
            x = int(input(f"insira a nota {i+1} "))
            if 0 <= x <= 10:
                soma += x
                aluno.append(x)
                break
    aluno.append(soma/3)
    return aluno

def verificador(x,y,n, z):
    while True:
        opcao = input(z).upper()
        if opcao == x or opcao == y or opcao == n:
            break
    return opcao

# main --------------------------------------------

todosAlunos = []
print("para finalizar, digite 0")

while True:
    verifica = verificador("A", "C", "0", "deseja adicionar ou consultar? (A/C) ")
    if verifica == "0":
        break
    elif verifica == "A":
        adiciona()
    else:
        consulta()
