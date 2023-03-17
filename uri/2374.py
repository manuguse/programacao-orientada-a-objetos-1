# exemplo 2374

N = int(input('pressão desejada '))
while (N < 1) or (N > 40):
    print('valor inválido')
    N = int(input('pressão desejada '))

M = int(input('pressão lida '))
while (M < 1) or (M > 40):
    print('valor inválido')
    M = int(input('pressão lida '))

diferenca = int(N - M)
print(diferenca)
