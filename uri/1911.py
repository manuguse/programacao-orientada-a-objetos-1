def verificaNum(a,b):
    while True:
        x = int(input())
        if a <= x <= b:
            break
    return x

while True:

    originais = {}
    aula = {}
    somaFalsa = 0

    n = verificaNum(0,50)
    if n == 0:
        break
    for i in range(n):
        nomeAssin = input().split(" ")
        originais[nomeAssin[0]] = nomeAssin[1] 

    m = verificaNum(1,n)
    for i in range(m):
        nomeAssin = input().strip().split(" ")
        aula[nomeAssin[0]] = nomeAssin[1] 
        if aula[nomeAssin[0]] != originais[nomeAssin[0]]:
            somaFalsa += 1
 
    print(somaFalsa)
