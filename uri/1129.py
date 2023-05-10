x = ("A","B","C","D","E")

while True:
    while True:
        numQuestoes = int(input())
        if 0 <= numQuestoes <= 255:
            break

    if numQuestoes == 0:
        break

    for i in range(numQuestoes):
        respostas = input().split(" ")
        preto = 0
        for j in range(5):
            if int(respostas[j]) <= 127:
                preto += 1
                respostaMarcada = j
        if preto == 1:
            print(x[respostaMarcada])
        else:
            print("*")
