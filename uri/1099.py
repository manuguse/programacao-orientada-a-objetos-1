num = int(input('numero de testes: '))

for i in range(num):
    somaImpar = 0
    x = int(input())
    y = int(input())
    if x < y:
        inicial = x + 1
        final = y
    if x > y:
        inicial = y + 1
        final = x
    if x == y:
        print("soma: 0")
        continue
    for i in range(inicial,final):
        if (i%2 != 0):
            somaImpar += i
    print('soma:',somaImpar)
