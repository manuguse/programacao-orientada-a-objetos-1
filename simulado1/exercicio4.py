def encontraPrimos(n):
    while True:
        cont = 0
        for i in range (2, n):
            if n % i == 0:
                cont += 1
        if cont == 0:
            tipo = 'primo'
            return n
            break
        n -= 1

X = int(input('numero de verificacoes '))

for i in range (X):
    while True:
        N, M = input('N e M: ').split(' ')
        N = int(N)
        M = int(M)
        if 2 <= N <= 100 and 2 <= M <= 100:
            break
        print('valor(es) invalido(s)')

    encontraPrimos(N)
    primoN = (encontraPrimos(N))
    
    encontraPrimos(M)
    primoM = (encontraPrimos(M))

    resp = (primoN) * (primoM)
    
    print(resp)
    
print('fim')
