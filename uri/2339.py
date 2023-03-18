# exercício 21 (2339)

C = int(input("número de competidores "))
while (C >1000) or (C < 1):
    print('valor inválido')
    C = int(input("número de competidores "))

P = int(input("folhas compradas "))
while (P >1000) or (P < 1):
    print('valor inválido')
    P = int(input("folhas compradas "))

F = int(input("folhas necessárias para cada "))
while (F >1000) or (F < 1):
    print('valor inválido')
    F = int(input("folhas necessárias para cada "))

if (P/C >= F):
    print('S')
else:
    print('N')
