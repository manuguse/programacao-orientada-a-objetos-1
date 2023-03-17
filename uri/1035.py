# exercício 19 (1035)

A = int(input('valor de A '))
B = int(input('valor de B '))
C = int(input('valor de C '))
D = int(input('valor de D '))

if (B < C):
    print('valores não aceitos')
elif (D < A):
    print('valores não aceitos')
elif ((C + D)<(A + B)):
    print('valores não aceitos')
elif (C < 0) or (D < 0):
    print('valores não aceitos')
elif (A%2 != 0):
    print('valores não aceitos')
else:
    print('valores aceitos')
