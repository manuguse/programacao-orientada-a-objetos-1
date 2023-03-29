cont = 0
while True:
    n = int(input('bandejas '))
    if (1 <= n <= 100):
        break

for i in range(n):
    while True:
        lata = int(input('lata '))
        if (1 <= lata <= 100):
            break
    while True:
        copo = int(input('copo '))
        if (1 <= copo <= 100):
            break

    if lata > copo:
        cont += copo
print(cont)
