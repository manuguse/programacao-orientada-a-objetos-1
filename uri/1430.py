notas = {'W':1, 'H':1/2, 'Q':1/4, 'E':1/8, 'S':1/16, 'T':1/32, 'X':1/64}

def verificaNumComp():
    while True:
        x = input("")
        if 3 <= len(x) <= 200:
            break
        elif x == "*":
            break
        print("o valor deve estar entre 3 e 200")
    return x

while True:
    composicao = input().upper().split('/')
    if composicao[0] == "*":
        break
    contaCerto = 0

    for i in range(len(composicao)):
        soma = 0
        for j in range(len(composicao[i])):
            soma += notas[composicao[i][j]]
        if soma == 1:
            contaCerto += 1
    print(contaCerto)
