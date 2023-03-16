# exercício 2408

a = int(input('valor de a '))
while (a < 0) or (a > 100):
    print('valor inválido')
    a = int(input('valor de a '))

b = int(input('valor de b '))
while (b < 0) or (b > 100):
    print('valor inválido')
    b = int(input('valor de b '))

c = int(input('valor de c '))
while (c < 0) or (c > 100):
    print('valor inválido')
    c = int(input('valor de c '))

if (b>a>c) or (c>a>b):
    print(a)
elif (a>b>c) or (c>b>a):
    print(b)
else:
    print(c)
