def ordena():
    for i in range(n):
        for j in range(n):
            if int(v[i]) > int(v[j]):
                v[i], v[j] = v[j], v[i]
    return v

def verificaNum(a, b):
    while True:
         x = int(input())
         if a <= x <= b:
             break
    return x

def verificaNum2(n):
    while True:
        confere = 0
        x = input().split(" ")
        for i in range(n):
            if 1 <= int(x[i]) <= 10000:
                confere += 1
        if confere == n:
            break
    return x

while True:
    n = int(verificaNum(2, 1000))
    if n == 0:
        break
    v = verificaNum2(n)
    tupla = tuple(v)
    vOrd = ordena()
    assassino = str(vOrd[1])
    print(tupla.index(assassino) + 1)
