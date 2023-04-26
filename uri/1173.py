n = []

while True:
    v = int(input('valor '))
    if v <= 50:
        break
    
for i in range(11):
    if i == 0:
        n.append(v*2)
    else:
        n.append((n[i-1]) * 2)
    print(f'N[{i}] = {n[i]}')
