# exercício 1038

x = int(input('x '))
while(x < 1) or (x > 5):
    print('valor inválido')
    x = int(input('x '))

y = float(input('y '))

if (x == 1):
    valor = 4*y
elif (x == 2):
    valor = 4.5*y
elif (x == 3):
    valor = 5*y
elif (x == 4):
    valor = 2*y
elif (x == 5):
    valor = 1.5*y
    
print('total: R$ {:.2f}'.format(valor))
