n = int(input('num idas à feira '))

for i in range(n):
    produto = {}
    m = int(input('num produtos disponiveis '))
    for i in range(m):
        x = input().split()
        produto[x[0]] = x[1]
        print(produto)
    p = int(input('num produtos para comprar '))
    valor = 0
    for i in range(p):
        y = input().split()
        valor += (float(produto[y[0]])*int(y[1]))

    print(f'R$: {valor:.2f}')
