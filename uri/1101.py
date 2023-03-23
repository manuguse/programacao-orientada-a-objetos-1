# exercício 1101

while True:
    soma = 0
    M = int(input('valor de M '))
    N = int(input('valor de N '))

    if N <= 0:
        break
    elif N <= 0:
        break
    
    elif N < M:
        inicial = N
        final = M + 1
    elif M < N:
        inicial = M
        final = N + 1

    for i in range (inicial,final):
        soma += i
        print(i, end=' ')

    print(f'soma = {soma}')
