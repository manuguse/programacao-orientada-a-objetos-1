def verifica(x, num):
    if x%num == 0:
        return 1
    else:
        return 0

while True:
    n = int(input())
    if 1 <= n <= 1000:
        break

while True:
    confere = 0
    l = input().split(" ")
    if len(l) != n:
        continue
    for i in range(n):
        if 1 <= int(l[i]) <= 100:
            confere += 1
    if confere == n:
        break
    
soma2 = 0
soma3 = 0
soma4 = 0
soma5 = 0
    
for i in range(n):
    x = int(l[i])
    soma2 += int(verifica(x, 2))
    soma3 += int(verifica(x, 3))
    soma4 += int(verifica(x, 4))
    soma5 += int(verifica(x, 5))

print(f'{soma2} multiplo(s) de 2')
print(f'{soma3} multiplo(s) de 3')
print(f'{soma4} multiplo(s) de 4')
print(f'{soma5} multiplo(s) de 5')
