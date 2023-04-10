while True:
    N = int(input('pessoas detectadas '))
    if 1 <= N <= 10:
        break
    print('valor invalido')

somaTempo = 0
t1 = 0
t2 = 0

for i in range(N):
    while True:
        T = int(input('ultimo instante '))
        if 0 <= T <= 100:
            break
        print('valor invalido')
    
    t2 = T
    
    if i == 0:
        somaTempo += 10
    elif t2 - t1 <= 10:
        somaTempo += (t2 - t1)
    else:
        somaTempo += t2
            
    t1 = T
    
print(somaTempo)
