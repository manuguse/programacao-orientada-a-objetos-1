from random import randrange

num = randrange(11)
cont = 1
tent = int(input('insira sua tentativa '))
while (tent > 10) or (tent < 0):
    print('numero inválido')
    tent = int(input('insira sua tentativa '))
    
while (num != tent):
    tent = int(input('tente novamente '))
    while (tent > 10) or (tent < 0):
        print('numero inválido')
        tent = int(input('insira sua tentativa '))
    cont += 1
print('você conseguiu!\no seu número de tentativas foi {}'.format(cont))
