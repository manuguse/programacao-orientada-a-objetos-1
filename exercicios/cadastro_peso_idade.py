def ordenaPesos():
    peso = pessoas[:]
    for i in range(n):
        for j in range(n):
            if int(peso[i][2]) > int(peso[j][2]):
                peso[i], peso[j] = peso[j], peso[i]
    return peso

pessoas = []
soma20 = 0
mais20 = []

while True:
    n = int(input("qtde de pessoas "))
    for i in range(n):
        infos = []
        infos.append(input("nome "))
        infos.append(int(input("idade ")))
        infos.append(float(input("peso ")))
        pessoas.append(infos[:])

    peso = ordenaPesos()

    print(f"{len(pessoas)} pessoas foram cadastradas")
    print(f"a pessoa mais pesada é {peso[0][0]} e tem {peso[0][2]}kg")
    print(f"a pessoa mais leve é {peso[-1][0]} e tem {peso[-1][2]}kg")

    for i in range(len(pessoas)):
        if pessoas[i][1] > 20:
            soma20 += 1
            mais20.append(pessoas[i])

    print("pessoas com mais de 20 anos: ")
    existe = False
    for i in range(soma20):
        print(f"{mais20[i][0]}, {mais20[i][1]} anos")
        existe = True
    if existe == False:
        print("ninguem")

    while True:
        x = input("deseja continuar? (S/N) ")
        if x == "S" or x == "N":
            break
        
    if x == "N":
        break
