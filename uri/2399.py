def verificaNum():
    while True:
        x = int(input())
        if x == 0 or x == 1:
            break
    return x

celula = []
minas = []

while True:
    N = int(input())
    if 1 <= N <= 50:
        break

for i in range(N):
    celula.append(verificaNum())
    
for k in range(N):
    minas.append(0)
    if k == 0:
        if celula[k] == 1:
            minas[k] += 1
        if celula[k+1] == 1:
            minas[k] += 1
            
    elif k == (N-1):
        if celula[k] == 1:
            minas[k] += 1
        if celula[k-1] == 1:
            minas[k] += 1
            
    else:
        if celula[k] == 1:
            minas[k] += 1
        if celula[k+1] == 1:
            minas[k] += 1
        if celula[k-1] == 1:
            minas[k] += 1
    
    print(f'{minas[k]}')
