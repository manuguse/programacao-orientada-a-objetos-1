# exercício 1045

A = float(input('valor de A '))
while (A < 0):
    print('valor inválido')
    A = float(input('valor de A '))

B = float(input('valor de B '))
while (B < 0):
    print('valor inválido')
    B = float(input('valor de B '))
    
C = float(input('valor de C '))
while (C < 0):
    print('valor inválido')
    C = float(input('valor de C '))

if (A > C) and (A > B):
    if (A >= B + C):
        print('NAO FORMA TRIANGULO')
    elif (A**2 == B**2 + C**2):
        print('TRIANGULO RETANGULO')
    elif (A**2 > B**2 + C**2):
        print('TRIANGULO OBTUSANGULO')
    elif (A**2 < B**2 + C**2):
        print('TRIANGULO ACUTANGULO')

elif (B > A) and (B > C):
    if (B >= A + C):
        print('NAO FORMA TRIANGULO')
    elif (B**2 == A**2 + C**2):
        print('TRIANGULO RETANGULO')
    elif (B**2 > A**2 + C**2):
        print('TRIANGULO OBTUSANGULO')
    elif (B**2 < A**2 + C**2):
        print('TRIANGULO ACUTANGULO')
        
else:
    if (C >= A + B):
        print('NAO FORMA TRIANGULO')
    elif (C**2 == A**2 + B**2):
        print('TRIANGULO RETANGULO')
    elif (C**2 > A**2 + B**2):
        print('TRIANGULO OBTUSANGULO')
    elif (C**2 < A**2 + B**2):
        print('TRIANGULO ACUTANGULO')

if (A == B == C):
    print('TRIANGULO EQUILATERO')
elif (A == B) or (B == C) or (A == C):
    print('TRIANGULO ISOSCELES')
