N = int(input('insira um número '))
while (N <= 1) or (N >= 1000):
    print('valor inválido')
    N = int(input('insira um número '))
for i in range (1,11):
    r = (i*N)
    print(f'{i} X {N} = {r}')
