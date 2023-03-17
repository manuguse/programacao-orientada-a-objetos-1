# exemplo 1012

A = float(input('valor de A '))
B = float(input('valor de B '))
C = float(input('valor de C '))
pi = 3.14159
    
areaTriangulo = float(A*C/2)
areaCirculo = float(pi*(C**2))
areaTrapezio = float((A + B)*C/2)
areaQuadrado = float(B**2)
areaRetangulo = float(A * B)

print('TRIANGULO = {:.3f}'.format(areaTriangulo))
print('CIRCULO = {:.3f}'.format(areaCirculo))
print('TRAPEZIO = {:.3f}'.format(areaTrapezio))
print('QUADRADO = {:.3f}'.format(areaQuadrado))
print('RETANGULO = {:.3f}'.format(areaRetangulo))
