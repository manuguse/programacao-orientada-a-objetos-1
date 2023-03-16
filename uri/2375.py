# exercício 2375

N = int(input('diâmetro '))
while (N < 1) or (N > 10000):
    print('valor inválido')
    N = int(input('diâmetro '))

A = int(input('altura '))
while (A < 1) or (A > 10000):
    print('valor inválido')
    A = int(input('altura '))

L = int(input('largura '))
while (L < 1) or (L > 10000):
    print('valor inválido')
    L = int(input('largura '))

P = int(input('profundidade '))
while (P < 1) or (P > 10000):
    print('valor inválido')
    P = int(input('profundidade '))

if (N > A):
    print('N')
elif (N > L):
    print('N')
elif (N > P):
    print('N')
else:
    print('S')
