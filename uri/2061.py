while True:
    N = int(input('numero inicial '))
    if (0 < N < 500):
        break
while True:
    M = int(input('acoes realizadas '))
    if (0 < M < 500):
        break

for i in range (M):
    while True:
        acao = str(input('acao ')).upper()
        if (acao == 'F') or (acao == 'C'):
            break
    if acao == 'F':
        N += 1
    elif acao == 'C':
        N -= 1

print(N)
