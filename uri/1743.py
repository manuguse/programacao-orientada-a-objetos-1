# uri 1743

def verificaNum(a):
    while True:
        cont = 0
        k = input(f'insira {a} ').split(' ')
        if len(k) != 5:
            continue
        for i in range(5):
            if 0 <= int(k[i]) <= 1:
                cont += 1            
        if cont == 5:a
            break           
    return k

x = verificaNum('x')
y = verificaNum('y')
contStatus = 0

for i in range(5):
    if int(x[i]) != int(y[i]):
        contStatus += 1

if contStatus == 5:
    print('Y')
else:
    print('N')
