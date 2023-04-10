T = int(input('numero de instancias: '))
for i in range(T):
    while True:
        C, D = input('C, D ').split(' ')
        C = int(C)
        D = int(D)
        if 0 <= C <= 6 and 0 <= D <= 9:
            break
        print('valor(es) inválido(s)')
    if C and D > 0:
        placas = 26**C * 10**D
    elif C > 0:
        placas = 26**C
    elif D > 0:
        placas = 10**D
    else:
        placas = 0
    print(placas)
