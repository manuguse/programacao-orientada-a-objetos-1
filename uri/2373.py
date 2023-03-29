cont = 0
n = int(input('bandejas '))

for i in range(n):
    lata = int(input('lata '))
    copo = int(input('copo '))
    if lata > copo:
        cont += copo
print(cont)
